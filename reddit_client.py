import praw
from env_loader import load_env

env = load_env()

try:
    reddit = praw.Reddit(
        client_id=env["REDDIT_CLIENT_ID"],
        client_secret=env["REDDIT_SECRET"],
        username=env["REDDIT_USERNAME"],
        password=env["REDDIT_PASSWORD"],
        user_agent=env["USER_AGENT"]
    )

    # Confirm Reddit credentials and subreddit access
    print(f"[Reddit] Logged in as u/{reddit.user.me()}")
    subreddit = reddit.subreddit(env["SUBREDDIT"])
    print(f"[Reddit] Watching subreddit: r/{env['SUBREDDIT']}")

except Exception as e:
    print(f"[Reddit Init Error] {e}")
    raise