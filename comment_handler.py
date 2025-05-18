import re
import random
import time
import traceback
from reddit_client import reddit, subreddit
from youtube_client import search_youtube_video
from genre_detector import detect_genres
from formatter import format_reply
from dedication_tracker import handle_dedication
from snark_pool import get_snark_reply

processed_comments = set()
user_song_history = {}

def handle_comment(comment):
    try:
        if comment.id in processed_comments:
            return
        if not comment.body.lower().startswith("yachtthot play"):
            return

        query = comment.body[len("yachtthot play"):].strip()
        if not query:
            return

        print(f"[Comment] Checking comment: {comment.body} by u/{comment.author}")
        video_details = search_youtube_video(query)
        if not video_details:
            print("[YouTube Search Error] No results found.")
            comment.reply("**NOW PLAYING:**\n\nNothing. You gave me nothing to work with.\n\n0:01 / 0:00")
            processed_comments.add(comment.id)
            return

        title = video_details["title"]
        url = video_details["link"]
        author_name = str(comment.author)

        genres = detect_genres(title)
        print(f"[Genres Detected] {genres}")

        dedication_target = handle_dedication(comment)

        song_key = f"{author_name}:{title.lower()}"
        repeat_request = song_key in user_song_history
        user_song_history[song_key] = True

        snark_triggered = False
        snark_override = None

        if dedication_target:
            snark_override = f"dedication::{dedication_target}"
            snark_triggered = True
        elif repeat_request and random.random() < 0.25:
            snark_override = "repeat"
            snark_triggered = True
        elif genres and random.random() < 0.25:
            snark_override = genres[0]
            snark_triggered = True
        elif random.random() < 0.25:
            snark_override = "random"
            snark_triggered = True

        snark_line = get_snark_reply(snark_override) if snark_triggered else None
        reply = format_reply(title, url, snark_line)
        comment.reply(reply)
        processed_comments.add(comment.id)

    except Exception as e:
        print(f"[Main Loop Error] {e}")
        traceback.print_exc()

def main():
    print("[YachtThot] Watching subreddit:", subreddit.display_name)
    while True:
        try:
            for comment in subreddit.stream.comments(skip_existing=True):
                handle_comment(comment)
        except Exception as e:
            print(f"[Stream Error] {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()