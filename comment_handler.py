import re
from youtube_client import get_video_details
from formatter import format_reply
from spotify_client import get_genres_for_song

def handle_comment(comment):
    if re.match(r"(?i)^YachtThot play ", comment.body):
        query = re.sub(r"(?i)^YachtThot play ", "", comment.body).strip()
        video = get_video_details(query)
        if video:
            genres = get_genres_for_song(video["title"])
            reply = format_reply(video, genres=genres)
            comment.reply(reply)