import re
from youtube_client import get_video_details
from formatter import format_reply
from spotify_client import get_genres_for_song

def handle_comment(comment):
    # Avoid replying to the bot's own comments
    if str(comment.author).lower() == "yacht_test_bot":
        return

    if re.match(r"(?i)^YachtThot play ", comment.body):
        query = re.sub(r"(?i)^YachtThot play ", "", comment.body).strip()
        video = get_video_details(query)

        if video:
            # DEBUG: Print YouTube title
            print(f"Fetching genres for: {video['title']}")
            genres = get_genres_for_song(video["title"])

            # DEBUG: Show genres returned by Spotify
            print("Genres returned:", genres)

            # Always include snark for testing (temporarily)
            reply = format_reply(video, snark_override="This song is so genre-bad Spotify tried to genre-ban it.")

            # Uncomment this for conditional snark later
            # snark = None
            # if any(g in genres for g in ["butt rock", "post-grunge", "cringe pop"]):
            #     snark = "Spotify says this genre has been reported to HR."
            # reply = format_reply(video, snark_override=snark)

            comment.reply(reply)