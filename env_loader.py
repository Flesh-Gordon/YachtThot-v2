from dotenv import load_dotenv
import os

def load_env(path=".env"):
    load_dotenv(dotenv_path=path)
    return {
        "REDDIT_CLIENT_ID": os.getenv("REDDIT_CLIENT_ID"),
        "REDDIT_SECRET": os.getenv("REDDIT_SECRET"),
        "REDDIT_USERNAME": os.getenv("REDDIT_USERNAME"),
        "REDDIT_PASSWORD": os.getenv("REDDIT_PASSWORD"),
        "USER_AGENT": os.getenv("USER_AGENT"),
        "YOUTUBE_API_KEY": os.getenv("YOUTUBE_API_KEY"),
        "SPOTIFY_CLIENT_ID": os.getenv("SPOTIFY_CLIENT_ID"),
        "SPOTIFY_CLIENT_SECRET": os.getenv("SPOTIFY_CLIENT_SECRET"),
        "SUBREDDIT": os.getenv("SUBREDDIT"),
    }