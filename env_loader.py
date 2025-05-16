from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {
        "REDDIT_CLIENT_ID": os.getenv("REDDIT_CLIENT_ID"),
        "REDDIT_SECRET": os.getenv("REDDIT_SECRET"),
        "REDDIT_USERNAME": os.getenv("REDDIT_USERNAME"),
        "REDDIT_PASSWORD": os.getenv("REDDIT_PASSWORD"),
        "USER_AGENT": os.getenv("USER_AGENT"),
        "YOUTUBE_API_KEY": os.getenv("YOUTUBE_API_KEY"),
        "SUBREDDIT": os.getenv("SUBREDDIT"),
    }
