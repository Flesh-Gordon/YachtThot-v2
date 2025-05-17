import re
import random
import os
from youtube_client import search_youtube_video
from formatter import format_reply
from spotify_client import get_genres_for_song
from snark_pool import get_genre_snark, get_fallback_snark

def handle_comment(comment):
    # Avoid replying to itself based on the .env username
    if str(comment.author).lower() == os.getenv("REDDIT_USERNAME", "").lower():
        return

    # Match "YachtThot play [song]" requests
    if re.match(r"(?i)^YachtThot play ", comment.body):
        query = re.sub(r"(?i)^YachtThot play ", "", comment.body).strip()
        video = search_youtube_video(query)

        if video:
            print(f"Fetching genres for: {video['title']}")
            genres = get_genres_for_song(video["title"])
            print("Genres returned:", genres)

            # Try genre-based snark
            snark = get_genre_snark(genres)

            # If no genre match, apply fallback snark 25% of the time
            if not snark and random.random() < 0.25:
                snark = get_fallback_snark()

            reply = format_reply(video, snark_override=snark)
            comment.reply(reply)