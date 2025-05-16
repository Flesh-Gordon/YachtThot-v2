import praw
from env_loader import load_env

env = load_env()

reddit = praw.Reddit(
    client_id=env["REDDIT_CLIENT_ID"],
    client_secret=env["REDDIT_SECRET"],
    username=env["REDDIT_USERNAME"],
    password=env["REDDIT_PASSWORD"],
    user_agent=env["USER_AGENT"]
)

subreddit = reddit.subreddit(env["SUBREDDIT"])
