# youtube_client.py

from youtubesearchpython import VideosSearch

def search_youtube_video(query):
    try:
        videos_search = VideosSearch(query, limit=5)
        results = videos_search.result().get('result', [])

        for video in results:
            title = video['title']
            link = video['link']
            duration = video['duration']
            channel = video['channel']['name']

            # Prioritize official uploads if artist name is in the title
            if query.lower().split(" by ")[-1] in title.lower():
                return {
                    'title': title,
                    'url': link,
                    'duration': duration,
                    'channel': channel
                }

        # Fallback to first result
        if results:
            video = results[0]
            return {
                'title': video['title'],
                'url': video['link'],
                'duration': video['duration'],
                'channel': video['channel']['name']
            }

        return None
    except Exception as e:
        print(f"[YouTube Search Error] {e}")
        return None