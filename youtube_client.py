from googleapiclient.discovery import build
from env_loader import load_env

env = load_env()

def get_video_details(query):
    youtube = build("youtube", "v3", developerKey=env["YOUTUBE_API_KEY"])
    search = youtube.search().list(q=query, part="snippet", type="video", maxResults=1).execute()
    items = search.get("items", [])
    if not items:
        return None
    video_id = items[0]["id"]["videoId"]
    title = items[0]["snippet"]["title"]
    video = youtube.videos().list(part="contentDetails", id=video_id).execute()
    duration = video["items"][0]["contentDetails"]["duration"]
    return {"title": title, "id": video_id, "duration": duration}
