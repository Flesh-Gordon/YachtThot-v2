import yt_dlp

def search_youtube_video(query):
    try:
        # Configure yt_dlp options
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'extract_flat': True,
            'format': 'bestaudio/best',
        }

        # Perform a YouTube search
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(f"ytsearch5:{query}", download=False)
            videos = result.get("entries", [])
            if not videos:
                return None

            # Try to match based on " by Artist" in query
            if " by " in query:
                artist = query.lower().split(" by ")[-1]
                for video in videos:
                    if artist in video.get("title", "").lower():
                        return format_video_result(video)

            # Fallback: return first result
            return format_video_result(videos[0])

    except Exception as e:
        print(f"[yt_dlp Error] {e}")
        return None

def format_video_result(video):
    return {
        "title": video.get("title"),
        "url": f"https://www.youtube.com/watch?v={video.get('id')}",
        "duration": parse_duration(video.get("duration")),
        "channel": video.get("uploader"),
        "id": video.get("id")
    }

def parse_duration(seconds):
    try:
        if seconds is None:
            return "0:00"
        minutes = seconds // 60
        sec = seconds % 60
        return f"{minutes}:{sec:02d}"
    except:
        return "0:00"