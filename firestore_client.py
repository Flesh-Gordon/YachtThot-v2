import firebase_admin
from firebase_admin import credentials, firestore
import os
import datetime

# Load credentials
if not firebase_admin._apps:
    cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
    firebase_admin.initialize_app(cred)

db = firestore.client()

def log_rating(user, song_title, rating, comment_id):
    db.collection("ratings").add({
        "user": user,
        "song": song_title,
        "rating": rating,
        "comment_id": comment_id,
        "timestamp": datetime.datetime.utcnow()
    })

def get_average_rating(song_title):
    ratings_ref = db.collection("ratings").where("song", "==", song_title)
    docs = ratings_ref.stream()
    ratings = [doc.to_dict().get("rating", 0) for doc in docs]
    if ratings:
        avg = sum(ratings) / len(ratings)
        return round(avg, 2), len(ratings)
    return None, 0