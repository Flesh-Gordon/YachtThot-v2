from reddit_client import reddit, subreddit
from comment_handler import handle_comment
import time

print("YachtThot bot is running...")

for comment in subreddit.stream.comments(skip_existing=True):
    print(f"Checking comment: {comment.body} by u/{comment.author}")
    handle_comment(comment)
