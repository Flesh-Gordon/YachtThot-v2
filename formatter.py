from utils import parse_duration, build_media_bar

def format_reply(video, snark_override=None):
    duration = parse_duration(video["duration"])
    bar = build_media_bar(duration)

    return f"""**NOW PLAYING:**

[{video['title']}](https://www.youtube.com/watch?v={video['id']})

{bar}  0:01 / {duration}

{snark_override if snark_override else ""}
"""