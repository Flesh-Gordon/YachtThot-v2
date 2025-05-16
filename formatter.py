from utils import parse_duration, build_media_bar

def format_reply(video):
    duration = parse_duration(video["duration"])
    bar = build_media_bar(duration)
    return f"""tЯΔppΞd ιn ﬡlεsHgoяdoИ's bΔsΞmΞn†

**NOW PLAYING:**

[The Black Eyed Peas - {video['title']}](https://www.youtube.com/watch?v={video['id']})

{bar}  0:01 / {duration}
"""
