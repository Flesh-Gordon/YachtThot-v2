import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from reddit_client import reddit, subreddit
from comment_handler import handle_comment

print("YachtThot bot is running...")

while True:
    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            print(f"Checking comment: {comment.body} by u/{comment.author}")
            handle_comment(comment)
    except Exception as e:
        print(f"[Main Loop Error] {e}")
        time.sleep(5)  # pause briefly before retrying