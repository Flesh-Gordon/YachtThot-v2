from reddit_client import reddit, subreddit
from comment_handler import handle_comment
import time

print("YachtThot bot is running...")

for comment in subreddit.stream.comments(skip_existing=True):
    handle_comment(comment)
