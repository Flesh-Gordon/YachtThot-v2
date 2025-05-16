import os
import requests
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_spotify_token():
    auth_url = "https://accounts.spotify.com/api/token"
    response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET,
    })
    response.raise_for_status()
    return response.json()['access_token']

def search_track(query, token):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "type": "track", "limit": 1}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    items = response.json().get('tracks', {}).get('items', [])
    if not items:
        return None
    track = items[0]
    return {
        "track_id": track["id"],
        "name": track["name"],
        "artist_id": track["artists"][0]["id"],
        "artist_name": track["artists"][0]["name"]
    }

def get_artist_genres(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("genres", [])

def get_genres_for_song(query):
    token = get_spotify_token()
    track = search_track(query, token)
    if not track:
        return []
    return get_artist_genres(track['artist_id'], token)
