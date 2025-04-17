def get_css():
    return """
    <style>
        /* Global Styles - Dark Mode Friendly */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
            color: #E2E8F0;
            line-height: 1.6;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5 {
            font-weight: 700;
            margin-bottom: 1rem;
            color: #F1F5F9;
        }
        
        h1 {
            font-size: 2.5rem;
        }
        
        h2 {
            font-size: 2rem;
        }
        
        /* Button styling */
        .stButton button {
            background-color: #3B82F6;
            color: white;
            font-weight: 500;
            border-radius: 0.375rem;
            border: none;
            padding: 0.5rem 2rem;
            transition: all 0.3s;
            width: 100%;
        }
        
        .stButton button:hover {
            background-color: #2563EB;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        }
        
        /* Player Card Styling */
        .player-card {
            background-color: #1E293B;
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
            transition: all 0.2s;
            border-left: 3px solid #3B82F6;
        }
        
        .player-card:hover {
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transform: translateY(-2px);
        }
        
        /* Player Name and Rating */
        .player-name {
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.25rem;
            display: inline-block;
            width: 80%;
            color: #F1F5F9;
        }
        
        .player-info-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
        }
        
        .timestamp {
            font-size: 0.85rem;
            color: #94A3B8;
            font-style: italic;
            margin-left: 5px;
        }
        
        /* Rating colors - Dark mode friendly */
        .rating-poor {
            font-weight: 700;
            color: #ffffff;
            background-color: #DC2626;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 1rem;
            display: inline-block;
            text-align: center;
            min-width: 2rem;
            float: right;
        }
        
        .rating-below-average {
            font-weight: 700;
            color: #ffffff;
            background-color: #EA580C;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 1rem;
            display: inline-block;
            text-align: center;
            min-width: 2rem;
            float: right;
        }
        
        .rating-average {
            font-weight: 700;
            color: #000000;
            background-color: #FBBF24;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 1rem;
            display: inline-block;
            text-align: center;
            min-width: 2rem;
            float: right;
        }
        
        .rating-good {
            font-weight: 700;
            color: #ffffff;
            background-color: #059669;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 1rem;
            display: inline-block;
            text-align: center;
            min-width: 2rem;
            float: right;
        }
        
        .rating-excellent {
            font-weight: 700;
            color: #ffffff;
            background-color: #047857;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 1rem;
            display: inline-block;
            text-align: center;
            min-width: 2rem;
            float: right;
        }
        
        /* Team Header */
        .team-header {
            background-color: #1E40AF;
            color: white;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            text-align: center;
            font-size: 1.2rem;
            font-weight: 600;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        
        /* Match Summary */
        .match-summary {
            background-color: #1E293B;
            color: #F1F5F9;
            padding: 1.5rem;
            border-left: 5px solid #3B82F6;
            margin-bottom: 2rem;
            border-radius: 0 8px 8px 0;
            line-height: 1.8;
        }
        
        /* Analysis Time */
        .analysis-time {
            font-style: italic;
            color: #94A3B8;
            text-align: right;
            margin-top: 1rem;
        }
        
        /* Match Header */
        .match-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Score Display */
        .score-display {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 1rem 0;
            background-color: #0F172A;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            border: 1px solid #334155;
        }
        
        .team-name {
            font-size: 1.5rem;
            font-weight: 700;
            width: 40%;
            text-align: center;
            color: #F1F5F9;
        }
        
        .score {
            font-size: 3.5rem;
            font-weight: 800;
            margin: 0 1rem;
            width: 20%;
            text-align: center;
            color: #F1F5F9;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        }
        
        /* Expander Styling */
        .streamlit-expanderHeader {
            font-weight: 500;
            color: #60A5FA;
        }
        
        .streamlit-expanderContent {
            background-color: #0F172A;
            padding: 0.75rem;
            border-radius: 0.375rem;
            color: #E2E8F0;
        }
        
        /* Input Field Styling */
        .stTextInput input {
            border-radius: 0.375rem;
            border: 1px solid #475569;
            padding: 0.75rem;
            transition: all 0.3s;
            background-color: #1E293B;
            color: #F1F5F9;
        }
        
        .stTextInput input:focus {
            border-color: #60A5FA;
            box-shadow: 0 0 0 2px rgba(96, 165, 250, 0.2);
        }
        
        /* Make the video sticky so it stays in view - improved */
        .sticky-video {
            position: sticky;
            top: 0;
            z-index: 999;
            background-color: #0F172A;
            padding-bottom: 1rem;
            margin-bottom: 1rem;
            height: fit-content;
        }
        
        /* Ensure the left column content has proper height and scroll behavior */
        .left-column-content {
            position: relative;
            display: flex;
            flex-direction: column;
        }
        
        /* Set proper overflow behavior for main containers */
        [data-testid="stVerticalBlock"] {
            gap: 0;
        }
        
        /* Make sure the main block knows its height */
        .main-block {
            height: 100vh;
            overflow: hidden;
        }
        
        /* Ensure iframe takes proper space */
        .sticky-video iframe {
            width: 100%;
            height: 400px;
            max-height: 50vh;
        }
        
        /* Custom styling for the tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #1E293B;
            border-radius: 8px 8px 0 0;
            border: none;
            padding: 0 20px;
            font-weight: 500;
            color: #94A3B8;
        }

        .stTabs [aria-selected="true"] {
            background-color: #3B82F6 !important;
            color: white !important;
        }
        
        /* Scrollable right panel - improved */
        .scrollable-panel {
            max-height: 90vh;
            overflow-y: auto;
            padding-right: 10px;
            display: block;
            position: relative;
        }
        
        /* Scrollbar styling */
        .scrollable-panel::-webkit-scrollbar {
            width: 8px;
        }
        
        .scrollable-panel::-webkit-scrollbar-track {
            background: #1E293B;
            border-radius: 8px;
        }
        
        .scrollable-panel::-webkit-scrollbar-thumb {
            background: #475569;
            border-radius: 8px;
        }
        
        .scrollable-panel::-webkit-scrollbar-thumb:hover {
            background: #64748B;
        }
        
        /* Key moments styling */
        .key-moment {
            background-color: #1E293B;
            padding: 0.5rem;
            border-radius: 4px;
            margin-bottom: 0.5rem;
            border-left: 2px solid #3B82F6;
        }
        
        .moment-timestamp {
            font-weight: 600;
            color: #60A5FA;
            display: inline-block;
            margin-right: 0.5rem;
        }
    </style>
    """