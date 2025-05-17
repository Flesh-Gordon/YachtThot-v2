import random

genre_snark_map = {
    "christian": [
        "This one goes out to the youth pastor with an acoustic guitar.",
        "Raise your hands... and lower your standards.",
        "Nothing like praising and cringing at the same time.",
        "The Holy Spirit just skipped this track."
    ],
    "pop": [
        "This is what plays in a Forever 21 dressing room.",
        "Manufactured serotonin, now in autoplay flavor.",
        "Basic. But okay.",
        "Catchy enough to hate yourself for liking it."
    ],
    "country": [
        "Boots, beer, breakup — yep, it's all here.",
        "You just yee’d your last haw.",
        "Let me guess, trucks and heartbreak?",
        "More twang than talent."
    ],
    "edm": [
        "When the bass drops, so does your dignity.",
        "This song glowsticks itself.",
        "You're not at Coachella. Stop."
    ],
    "butt rock": [
        "Your dad called. He wants his aux cord back.",
        "Unironically headbanging in a lifted Dodge Ram right now.",
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
        "Ah yes, the golden age of radio regret.",
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
        "This belongs on a playlist called ‘Regret in 3–5 business days.’",
        "It’s less ‘slow jam,’ more ‘slow cringe.’"
    ],
    "r&b": [
        "R&B used to be smooth. This is... sticky.",
        "Your hormones have awful taste.",
        "Let’s put the aux down and pick up a Bible."
    ],
    "comedy": [
        "Spotify filed this under 'accidents that sound like music.'",
        "It's giving: banned from open mic night."
    ],
    "cringe": [
        "If cringe had a soundtrack, this would be it.",
        "This song is why aux cords need background checks."
    ]
}

fallback_snark = [
    "You woke up and chose mediocrity.",
    "This song has main character energy... in a straight-to-DVD sequel.",
    "A bold choice. Not a good one, just bold.",
    "The audacity of this request is impressive.",
    "This track slaps like a wet sock."
]

def get_genre_snark(genres):
    if not genres:
        return None
    genres = [g.lower() for g in genres]
    for key in genre_snark_map:
        if any(key in g for g in genres):
            return random.choice(genre_snark_map[key])
    return None

def get_fallback_snark():
    return random.choice(fallback_snark)