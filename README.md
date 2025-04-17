# Football Video Analyst

A sophisticated football video analysis tool powered by Gemini 2.5 Pro and Streamlit.

## Overview

Football Video Analyst is an AI-powered application that automatically analyzes football match highlights from YouTube videos. The tool leverages Google's Gemini 2.5 Pro to provide detailed insights into team performances, player ratings, and key match moments. This application is designed for football analysts, coaches, enthusiasts, and anyone interested in getting in-depth analysis of football matches without manual effort.

## Features

- **Automated Video Analysis**: Process YouTube football highlight videos to extract comprehensive match insights
- **Team Identification**: Automatically identifies teams, players, scores, and competition information 
- **Player Performance Ratings**: Assigns ratings (1-10) to players based on their performance
- **Detailed Performance Analysis**: Provides detailed justification for each player's rating
- **Timestamp Identification**: Links analysis to specific timestamps in the video for key moments
- **Match Summary**: Delivers concise overview of the match with tactical observations
- **User-Friendly Interface**: Clean, intuitive Streamlit-based UI with embedded YouTube player

## Installation

```bash
# Clone the repository
git clone https://github.com/yYorky/FootballVideoAnalyst.git
cd footballvideoanalyst

# Install required dependencies
pip install -r requirements.txt
```

## Usage

1. Create a `.env` file in the root directory with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. In the web interface:
   - Enter a YouTube URL for football highlights
   - Click "Analyze Video" to process the content
   - View the detailed analysis across multiple tabs

## Configuration

- **API Key**: Requires a Google API key with access to Gemini 2.5 Pro model
- **Environment Variables**: Configure through a `.env` file
- **Model Selection**: Currently using `gemini-2.5-pro-exp-03-25` (can be updated in config.py)

## Directory Structure

```
football-video-analyst/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT license file
├── README.md              # Project documentation
├── modules/               # Project modules
│   ├── analysis.py        # Video analysis functionality
│   ├── config.py          # Configuration settings
│   ├── styles.py          # UI styling and CSS
│   ├── ui_components.py   # UI elements and components
│   └── video_utils.py     # YouTube video processing utilities
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Sam Witteveen](https://www.youtube.com/watch?v=pFpxpAMqSmU) for his video introducing Gemini2.5 Pro for Youtube Analysis
- [Google Gemini](https://ai.google.dev/) for the advanced AI model
- [Streamlit](https://streamlit.io/) for the web application framework
- [Github](https://github.com/) for the Copilot to allow me to vibecode directly with agents


