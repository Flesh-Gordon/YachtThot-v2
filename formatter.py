from utils import parse_duration, build_media_bar
import random
from snark_pool import get_snark_reply

genre_snark_map = {
    'brostep': "You're not in a warehouse rave. Turn this off.",
    'nightcore': "Seek help. Immediately.",
    'christian': "Nothing like praising and cringing at the same time.",
    'pop': "Basic. But okay.",
    'country': "Let me guess, trucks and heartbreak?",
    'dance pop': "This belongs in a Forever 21 changing room.",
    'edm': "When the bass drops, so does your dignity."
}

def format_reply(video, genres=None):
    duration = parse_duration(video["duration"])
    bar = build_media_bar(duration)

    # Determine snark: genre-based or random
    matched = [g for g in genres or [] if g in genre_snark_map]
    if matched:
        snark = genre_snark_map[matched[0]]
    else:
        snark = get_snark_reply() if random.random() < 0.25 else ""

    return f"""**NOW PLAYING:**

[{video['title']}](https://www.youtube.com/watch?v={video['id']})

{bar}  0:01 / {duration}

{snark}
"""
