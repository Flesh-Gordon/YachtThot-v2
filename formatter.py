from utils import parse_duration, build_media_bar
import random
from snark_pool import get_snark_reply

genre_snark_map = {
    "christian": [
        "Nothing like praising and cringing at the same time.",
        "Raise your hands — and your standards.",
        "The Holy Spirit just skipped this track."
    ],
    "pop": [
        "Basic. But okay.",
        "This is what plays in a Forever 21 dressing room.",
        "Catchy enough to hate yourself for liking it."
    ],
    "country": [
        "Let me guess, trucks and heartbreak?",
        "More twang than talent.",
        "Someone’s ex is crying into a beer right now."
    ],
    "edm": [
        "When the bass drops, so does your dignity.",
        "This song glowsticks itself.",
        "You're not at Coachella. Stop."
    ],
    "butt rock": [
        "Your dad called. He wants his aux cord back.",
        "Nickelback walked so this could limp.",
        "2003 called. It wants its flannel back."
    ],
    "dance pop": [
        "You could’ve picked *any* song. And you picked this.",
        "Great for cardio. Terrible for culture.",
        "Is this playing in a Planet Fitness right now?"
    ],
    "post-grunge": [
        "Post-grunge? More like post-good taste.",
        "This genre peaked at MySpace.",
        "Chad Kroeger is crying in a Camaro."
    ],
    "nightcore": [
        "Seek help. Immediately.",
        "Sonic the Hedgehog would be embarrassed.",
        "You really said 'faster, worse, louder.'"
    ],
    "trap": [
        "Sounds like someone auto-tuned their therapy session.",
        "Every 808 in this track is ashamed.",
        "Congratulations — you've picked the musical equivalent of a vape pen."
    ],
    "metalcore": [
        "Is that a breakdown or a nervous one?",
        "This song punches drywall unironically.",
        "Growling doesn’t make it deep."
    ],
    "idol": [
        "Simultaneously for teens and 45-year-olds.",
        "Kawaii meets chaos.",
        "Your algorithm needs therapy."
    ],
    "indie": [
        "This song is wearing thrift store cardigans and gatekeeping.",
        "Yes, it sounds like the band works at a coffee shop.",
        "Is this on vinyl? Of course it is."
    ],
    "broadway": [
        "Every note is a cry for attention.",
        "You hear voices? That's just the cast again.",
        "Please stop belting. We're begging."
    ],
    "cringe pop": [
        "Unironically painful.",
        "TikTok wants it back.",
        "This is why aliens won’t visit."
    ],
    "pornogrind": [
    "I didn’t know your taste in music came with an NSFW tag.",
    "This track should be required to knock first.",
    "Even OnlyFans said ‘that’s a bit much.’"
    ],
    "strip club": [
    "This song smells like glitter and regret.",
    "Please turn this off — I can smell Axe through the screen.",
    "Someone’s definitely throwing singles at their phone right now."
    ],
    "bedroom pop": [
    "This isn’t romantic. It’s just sweaty.",
    "This track comes with a side of awkward eye contact.",
    "Sounds like someone made this while biting their lip in the mirror."
    ],
    "dirty south": [
    "You chose vibes over values. Respect.",
    "YachtThot isn't liable for what happens if this gets played out loud.",
    "This song needs an 18+ warning and a mop."
    ],
    "sex comedy": [
    "It’s giving incel with a SoundCloud.",
    "This track has the same energy as a fake moan.",
    "Are you okay? No seriously."
    ],
    "slow jam": [
    "Mood: candles, bad decisions, and ignored texts.",
    "This belongs on a playlist called ‘Regret in 3-5 business days.’",
    "It’s less ‘slow jam,’ more ‘slow cringe.’"
    ],
    "r&b": [
    "R&B used to be smooth. This is... sticky.",
    "Your hormones have awful taste.",
    "Let’s put the aux down and pick up a Bible."
    ]
    
}

def format_reply(video, genres=None):
    duration = parse_duration(video["duration"])
    bar = build_media_bar(duration)

    # Determine snark: genre-based or random
    matched = [g for g in (genres or []) if g.lower() in genre_snark_map]
    if matched:
        snark = genre_snark_map[matched[0]]
    else:
        snark = get_snark_reply() if random.random() < 0.25 else ""

    return f"""**NOW PLAYING:**

[{video['title']}](https://www.youtube.com/watch?v={video['id']})

{bar}  0:01 / {duration}

{snark}
"""
