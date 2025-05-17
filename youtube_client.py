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

            # Prioritize results that contain the artist name if formatted as "Song by Artist"
            if " by " in query:
                artist = query.lower().split(" by ")[-1]
                if artist in title.lower():
                    return {
                        'title': title,
                        'url': link,
                        'duration': duration,
                        'channel': channel
                    }

        # Fallback to first result if no artist-specific match found
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