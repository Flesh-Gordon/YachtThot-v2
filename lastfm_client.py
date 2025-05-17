import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LASTFM_API_KEY")
BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def get_lastfm_tags(track_title, artist_name=None):
    params = {
        "method": "track.gettoptags",
        "api_key": API_KEY,
        "format": "json",
        "track": track_title
    }

    if artist_name:
        params["artist"] = artist_name

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        tags = data.get("toptags", {}).get("tag", [])
        tag_list = [tag["name"].lower() for tag in tags if int(tag.get("count", 0)) > 10]

        return tag_list[:5]  # return top 5 tags max
    except Exception as e:
        print(f"[Last.fm Error] {e}")
        return []