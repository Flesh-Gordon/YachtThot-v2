import re
from lastfm_client import get_lastfm_tags

def clean_title_for_lastfm(title):
    # Remove content in parentheses or brackets, trim whitespace
    return re.sub(r"[\[\(].*?[\]\)]", "", title).strip()

def detect_genres_from_metadata(video_title, artist=None):
    """
    Given a YouTube video title and optional artist name,
    returns a list of genre tags using Last.fm.
    """
    cleaned_title = clean_title_for_lastfm(video_title)
    print(f"[Genre Detector] Cleaned title: {cleaned_title}")

    # If artist is provided separately, use it with track title
    if artist:
        genres = get_lastfm_tags(cleaned_title, artist)
    else:
        genres = get_lastfm_tags(cleaned_title)

    if not genres:
        print("[Genre Detector] No genres found.")
    else:
        print(f"[Genre Detector] Genres detected: {genres}")

    return genres