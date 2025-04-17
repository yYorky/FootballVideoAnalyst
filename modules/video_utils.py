import re

def extract_youtube_id(url):
    """
    Extract YouTube video ID from various YouTube URL formats
    """
    youtube_regex = (
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    match = re.search(youtube_regex, url)
    if match:
        return match.group(6)
    return None

def embed_youtube_video(youtube_url):
    """
    Generate HTML for embedded YouTube video
    """
    video_id = extract_youtube_id(youtube_url)
    if video_id:
        return f'<iframe width="100%" height="400" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'
    else:
        return "Invalid YouTube URL"

def format_video_timestamp(timestamp):
    """
    Format a timestamp for display
    """
    if not timestamp:
        return ""
    
    # Just return the timestamp as is, since we're using video timestamps
    return timestamp

def parse_video_timestamp_to_seconds(timestamp):
    """
    Parse a timestamp string (like "1:24") to seconds
    """
    if not timestamp:
        return 0
        
    time_parts = timestamp.split(":")
    seconds = 0
    
    if len(time_parts) == 2:  # MM:SS format
        try:
            seconds = int(time_parts[0]) * 60 + int(time_parts[1])
        except ValueError:
            return 0
    elif len(time_parts) == 3:  # HH:MM:SS format
        try:
            seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])
        except ValueError:
            return 0
            
    return seconds