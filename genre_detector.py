from spotify_client import get_genres_for_song
from lastfm_client import get_lastfm_tags

def detect_genre_tags(track_title):
    # Get genres from Spotify (artist-level)
    spotify_genres = get_genres_for_song(track_title)

    # Get tags from Last.fm (track-level)
    lastfm_tags = get_lastfm_tags(track_title)

    # Combine and deduplicate
    combined = list(set(spotify_genres + lastfm_tags))
    
    # Optional debug log
    print(f"[GenreDetector] Combined tags for '{track_title}': {combined}")
    
    return combined