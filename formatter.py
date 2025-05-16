from utils import parse_duration, build_media_bar
import random
from snark_pool import get_snark_reply

def format_reply(video):
    duration = parse_duration(video["duration"])
    bar = build_media_bar(duration)

    snark = get_snark_reply()  # always include snark for testing

    return f"""**NOW PLAYING:**

[{video['title']}](https://www.youtube.com/watch?v={video['id']})

{bar}  0:01 / {duration}

{snark}
"""