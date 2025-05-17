import random

# Genre-based snark pool
genre_snark_map = {
    "christian": [
        "This one goes out to the youth pastor with an acoustic guitar.",
        "Raise your hands... and lower your standards."
    ],
    "cringe": [
        "If cringe had a soundtrack, this would be it.",
        "This song is why aux cords need background checks."
    ],
    "butt rock": [
        "Your dad called. He wants his aux cord back.",
        "Unironically headbanging in a lifted Dodge Ram right now."
    ],
    "post-grunge": [
        "Post-grunge? More like post-good taste.",
        "Ah yes, the golden age of radio regret."
    ],
    "pop": [
        "This is what plays in a Forever 21 dressing room.",
        "Manufactured serotonin, now in autoplay flavor."
    ],
    "country": [
        "Boots, beer, breakup — yep, it's all here.",
        "You just yee’d your last haw."
    ],
    "comedy": [
        "Spotify filed this under 'accidents that sound like music.'",
        "It's giving: banned from open mic night."
    ]
}

# General snark fallback pool
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
    
def get_snark_reply(genres=None):
    return get_genre_snark(genres) or get_fallback_snark()