import os
import base64
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from project root
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_spotify_token():
    auth_url = "https://accounts.spotify.com/api/token"
    raw_auth = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    encoded_auth = base64.b64encode(raw_auth.encode()).decode()

    auth_header = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    print("\n--- Spotify Auth Request ---")
    print("POST Data:", data)
    print("----------------------------\n")

    response = requests.post(auth_url, headers=auth_header, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def get_genres_for_song(query):
    print(f"Fetching genres for: {query}")
    token = get_spotify_token()

    search_url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "type": "track", "limit": 1}

    search_response = requests.get(search_url, headers=headers, params=params)
    search_response.raise_for_status()
    results = search_response.json()

    if not results.get("tracks", {}).get("items"):
        print("[Spotify] No tracks found.")
        return []

    artist_id = results["tracks"]["items"][0]["artists"][0]["id"]
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"

    artist_response = requests.get(artist_url, headers=headers)
    artist_response.raise_for_status()
    artist_data = artist_response.json()

    return artist_data.get("genres", [])