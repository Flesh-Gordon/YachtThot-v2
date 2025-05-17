# genre_detector.py

import os
from dotenv import load_dotenv
import requests

load_dotenv()

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
LASTFM_URL = "http://ws.audioscrobbler.com/2.0/"

def get_lastfm_tags(track_title, artist_name=None):
    params = {
        "method": "track.gettoptags",
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "track": track_title
    }

    if artist_name:
        params["artist"] = artist_name

    try:
        response = requests.get(LASTFM_URL, params=params)
        data = response.json()

        tags = data.get("toptags", {}).get("tag", [])
        tag_list = [tag["name"].lower() for tag in tags if int(tag.get("count", 0)) > 10]

        top_tags = tag_list[:5]  # return top 5 tags max
        print(f"[Last.fm Tags] Tags for '{track_title}': {top_tags}")
        return top_tags

    except Exception as e:
        print(f"[Last.fm Error] {e}")
        return []

def detect_genres(track_title, artist_name=None):
    return get_lastfm_tags(track_title, artist_name)