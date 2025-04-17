import streamlit as st
import time

# Import modules
from modules.config import PAGE_CONFIG, init_gemini_client, MODEL_NAME
from modules.styles import get_css
from modules.video_utils import extract_youtube_id, embed_youtube_video
from modules.analysis import analyze_football_video
from modules.ui_components import (
    display_player_analysis, 
    display_match_header, 
    display_match_summary, 
    display_analysis_time, 
    display_error,
    welcome_message
)

# Apply page configuration
st.set_page_config(**PAGE_CONFIG)

# Apply custom CSS
st.markdown(get_css(), unsafe_allow_html=True)

# Initialize Gemini client
client = init_gemini_client()

# Main application logic
if client:
    # Input field and video in the sidebar
    with st.sidebar:
        st.title("⚽ Football Video Analyst")
        
        # URL input
        youtube_url = st.text_input("Enter YouTube URL of football highlights video")
        
        if youtube_url:
            video_id = extract_youtube_id(youtube_url)
            
            # Display the embedded video in the sidebar
            st.subheader("Video")
            st.markdown(embed_youtube_video(youtube_url), unsafe_allow_html=True)
            
            # Analysis button below the video
            analyze_clicked = st.button("Analyze Video")
            
            # Initialize session state for analysis data
            if "analysis_data" not in st.session_state:
                st.session_state.analysis_data = None
            
            # When Analyze button is clicked
            if analyze_clicked:
                if not video_id:
                    st.error("Invalid YouTube URL. Please provide a valid YouTube video link.")
                else:
                    # Start timer
                    start_time = time.time()
                    
                    with st.spinner("Analyzing football video with Gemini 2.5... This may take a minute."):
                        # Run analysis
                        st.session_state.analysis_data = analyze_football_video(youtube_url, client, MODEL_NAME)
                        
                        # Calculate elapsed time
                        elapsed_time = time.time() - start_time
                        st.session_state.elapsed_time = elapsed_time
                        
                        # Force a rerun to update the main area with the results
                        st.rerun()
            
            # Display analysis time in the sidebar if analysis has been performed
            if hasattr(st.session_state, 'elapsed_time') and st.session_state.analysis_data is not None:
                display_analysis_time(st.session_state.elapsed_time)
            
            # Footer in sidebar
            st.markdown("---")
            st.caption("Powered by Gemini 2.5 & Streamlit")
    
    # Display analysis results in the main area
    if youtube_url and st.session_state.analysis_data is not None:
        analysis_data = st.session_state.analysis_data
        
        # Set main area title
        st.title("Football Match Analysis")
        
        # Display results in a structured format
        if "error" in analysis_data:
            display_error(analysis_data["error"], analysis_data.get("raw_response"))
        else:
            # Extract competition and match details
            competition = analysis_data.get("competition", "")
            match_date = analysis_data.get("match_date", "")
            match_stage = analysis_data.get("match_stage", "")
            team1 = analysis_data.get("team1", {})
            team2 = analysis_data.get("team2", {})
            
            # Create tabs for organized view
            tab1, tab2 = st.tabs(["Match Overview", "Player Analysis"])
            
            with tab1:
                # Display match header with team names and scores
                display_match_header(competition, match_date, match_stage, team1, team2)
                
                # Display match summary
                display_match_summary(analysis_data.get("match_summary", ""))
            
            with tab2:
                # Create two columns for team analysis
                col1, col2 = st.columns(2)
                
                # Team 1 analysis
                with col1:
                    st.markdown(f'<div class="team-header">{team1.get("name", "Team 1")}</div>', unsafe_allow_html=True)
                    display_player_analysis(team1)
                
                # Team 2 analysis
                with col2:
                    st.markdown(f'<div class="team-header">{team2.get("name", "Team 2")}</div>', unsafe_allow_html=True)
                    display_player_analysis(team2)
            
            # Removed display_analysis_time from here (moved to sidebar)
    elif youtube_url:
        # Show message when video is loaded but not yet analyzed
        st.info("Click the 'Analyze Video' button in the sidebar to analyze the football match.")
    else:
        # Show welcome message when no URL is entered
        st.title("Football Video Analyst")
        welcome_message()
else:
    st.error("Google API Key not found in environment variables. Please create a .env file with GOOGLE_API_KEY=your_api_key")