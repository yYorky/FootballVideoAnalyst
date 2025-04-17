import streamlit as st
from modules.analysis import get_rating_class
from modules.video_utils import format_video_timestamp

def display_player_analysis(team_data, show_timestamps=True):
    """
    Display player analysis for a team
    """
    for player in team_data.get("players", []):
        with st.container():
            st.markdown(f'<div class="player-card">', unsafe_allow_html=True)
            
            # Player name and rating using HTML instead of nested columns
            rating_class = get_rating_class(player.get("rating", 5))
            st.markdown(f'''
            <div class="player-info-container">
                <span class="player-name">{player["name"]}</span>
                <span class="{rating_class}">{player.get("rating", "-")}</span>
            </div>
            ''', unsafe_allow_html=True)
            
            # Player analysis in expander
            with st.expander("View Analysis"):
                st.write(player.get("analysis", "No analysis available"))
                
                # Key moments with timestamps
                key_moments = player.get("key_moments", [])
                if key_moments and show_timestamps:
                    st.markdown("### Key Moments")
                    for moment in key_moments:
                        timestamp = moment.get("time", "")
                        description = moment.get("description", "")
                        
                        if timestamp:
                            formatted_timestamp = format_video_timestamp(timestamp)
                            st.markdown(f'''
                            <div class="key-moment">
                                <span class="moment-timestamp">{formatted_timestamp}</span>
                                {description}
                            </div>
                            ''', unsafe_allow_html=True)
                        else:
                            st.markdown(f"**Unknown timestamp** - {description}")
            
            st.markdown('</div>', unsafe_allow_html=True)

def display_match_header(competition, match_date, match_stage, team1, team2):
    """
    Display match header with team names and scores
    """
    team1_name = team1.get("name", "Team 1")
    team2_name = team2.get("name", "Team 2")
    team1_score = team1.get("score", "?")
    team2_score = team2.get("score", "?")
    
    st.markdown(f"""
    <div class="match-header">
        <div style="font-size: 1.2rem; font-weight: 500; color: #F1F5F9;">{competition} {match_date}</div>
        <div class="score-display">
            <div class="team-name">{team1_name}</div>
            <div class="score">{team1_score}</div>
            <div style="font-size: 2.5rem; margin: 0 0.5rem; color: #94A3B8;">-</div>
            <div class="score">{team2_score}</div>
            <div class="team-name">{team2_name}</div>
        </div>
        <div style="font-size: 1rem; color: #F1F5F9; margin-top: 0.5rem;">{match_stage}</div>
    </div>
    """, unsafe_allow_html=True)

def display_match_summary(match_summary):
    """
    Display match summary section
    """
    st.markdown("<h2>Match Analysis</h2>", unsafe_allow_html=True)
    
    # Fix for blank match summary
    if not match_summary or match_summary.strip() == "":
        match_summary = "Match summary not available from the analysis."
    
    st.markdown(f'<div class="match-summary">{match_summary}</div>', unsafe_allow_html=True)

def display_analysis_time(elapsed_time):
    """
    Display analysis generation time
    """
    st.markdown(f'<div class="analysis-time">Analysis generated in {elapsed_time:.2f} seconds</div>', unsafe_allow_html=True)

def display_error(error_msg, raw_response=None):
    """
    Display error message and raw response if available
    """
    st.error(error_msg)
    if raw_response:
        with st.expander("Show Raw Response"):
            st.code(raw_response)

def welcome_message():
    """
    Display welcome message when no video URL is provided
    """
    st.markdown("""
    <div style="padding: 2rem; text-align: center; color: #94A3B8;">
        <h3>Enter a YouTube URL to begin</h3>
        <p>Provide a link to a football highlights video to generate an AI-powered analysis.</p>
    </div>
    """, unsafe_allow_html=True)