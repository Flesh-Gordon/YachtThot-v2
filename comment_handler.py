import re
import random
from youtube_client import get_video_details
from formatter import format_reply
from spotify_client import get_genres_for_song

def handle_comment(comment):
    # Avoid replying to itself
    if str(comment.author).lower() == "yacht_test_bot":
        return

    # Match "YachtThot play [song]" requests
    if re.match(r"(?i)^YachtThot play ", comment.body):
        query = re.sub(r"(?i)^YachtThot play ", "", comment.body).strip()
        video = get_video_details(query)

        if video:
            print(f"Fetching genres for: {video['title']}")
            genres = get_genres_for_song(video["title"])
            print("Genres returned:", genres)

            # Snark map based on common genres
            genre_snark_map = {
                "christian": "This one goes out to the youth pastor with an acoustic guitar.",
                "cringe": "If cringe had a soundtrack, this would be it.",
                "butt rock": "Your dad called. He wants his aux cord back.",
                "post-grunge": "Post-grunge? More like post-good taste.",
                "pop": "This is what plays in a Forever 21 dressing room.",
                "country": "Boots, beer, breakup — yep, it's all here.",
                "comedy": "Spotify filed this under 'accidents that sound like music.'"
            }

            # Normalize genres for case-insensitive matching
            matched_genres = [g.lower() for g in genres]
            snark = None
            for key, line in genre_snark_map.items():
                if any(key in g for g in matched_genres):
                    snark = line
                    break

            # 25% chance fallback snark if no genre match
            if not snark and random.random() < 0.25:
                snark = "You woke up and chose mediocrity."

            reply = format_reply(video, snark_override=snark)
            comment.reply(reply)