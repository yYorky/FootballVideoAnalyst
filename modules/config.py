import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Page configuration
PAGE_CONFIG = {
    "page_title": "Football Video Analyst",
    "page_icon": "⚽",
    "layout": "wide"
}

# Get API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini client
def init_gemini_client():
    if API_KEY:
        return genai.Client(api_key=API_KEY)
    return None

# Gemini model name
MODEL_NAME = "gemini-2.5-pro-exp-03-25"