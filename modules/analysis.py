import json
import re
from google import genai
from google.genai import types

def get_rating_class(rating):
    """
    Determine the CSS class for rating display based on rating value
    """
    try:
        rating_float = float(rating)
        if rating_float < 4:
            return "rating-poor"
        elif rating_float < 5:
            return "rating-below-average"
        elif rating_float < 7:
            return "rating-average"
        elif rating_float < 9:
            return "rating-good"
        else:
            return "rating-excellent"
    except (ValueError, TypeError):
        return "rating-average"  # Default if rating can't be converted

def analyze_football_video(youtube_url, client, model_name):
    """
    Analyze a football video using Gemini API
    """
    prompt = """Analyze the following football highlights video in detail:

1. TEAM IDENTIFICATION:
   - Identify both teams playing in the match
   - List the full names of all identifiable players for each team seen in the video
   - Identify the final score of the match
   - Identify the competition, date or round of the match (if visible)

2. PLAYER RATINGS:
   - Assign a rating from 1-10 for each identified player
   - Be critical and demanding in your ratings - reserve scores of 8+ only for truly exceptional performances
   - Most players should receive ratings between 4-7 depending on their performance
   - Consider factors like goals, assists, key defensive plays, technical skills displayed, and mistakes made
   - Ratings should accurately reflect both positive contributions and errors

3. PERFORMANCE ANALYSIS:
   - For each player, provide a brief justification (2-3 sentences) for their rating
   - IMPORTANT: Include specific video timestamps (e.g., "1:45") for key moments or actions that influenced their rating
   - Highlight both positive and negative actions from the player
   - Be objective and critical in your assessment

4. MATCH SUMMARY:
   - Brief overview of the match based on the highlights
   - Mention key turning points, outstanding performances, or decisive moments
   - Include tactical observations where possible

Your response must be structured in this specific JSON format to be processed correctly:
{
  "match_summary": "Overview of the match...",
  "competition": "Name of competition (e.g. Champions League, Premier League)",
  "team1": {
    "name": "Team Name",
    "score": 0,
    "players": [
      {
        "name": "Player Name",
        "rating": 8.5,
        "analysis": "Detailed analysis of player performance...",
        "key_moments": [
          {"time": "1:24", "description": "Description of the action at this timestamp"},
          {"time": "2:45", "description": "Another key moment"}
        ]
      }
    ]
  },
  "team2": {
    "name": "Team Name",
    "score": 0,
    "players": [
      {
        "name": "Player Name",
        "rating": 7.5,
        "analysis": "Detailed analysis of player performance...",
        "key_moments": [
          {"time": "0:55", "description": "Description of the action at this timestamp"},
          {"time": "3:12", "description": "Another key moment"}
        ]
      }
    ]
  }
}

Important: Provide only the JSON with no additional text before or after. Ensure the match_summary field has detailed content.
Make sure to include the "key_moments" array for each player with timestamp and description of important actions.
"""

    try:
        # Generate content using Gemini
        response = client.models.generate_content(
            model=model_name,
            contents=types.Content(
                parts=[
                    types.Part(text=prompt),
                    types.Part(
                        file_data=types.FileData(file_uri=youtube_url)
                    )
                ]
            )
        )
        
        # Parse the JSON response
        try:
            analysis_json = json.loads(response.text)
            return analysis_json
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract JSON from the text response
            # This is a fallback in case the model doesn't return clean JSON
            json_text = re.search(r'({.*})', response.text, re.DOTALL)
            if json_text:
                try:
                    analysis_json = json.loads(json_text.group(1))
                    return analysis_json
                except:
                    pass
            return {"error": "Could not parse response as JSON", "raw_response": response.text}
    except Exception as e:
        return {"error": f"Error analyzing the video: {str(e)}"}