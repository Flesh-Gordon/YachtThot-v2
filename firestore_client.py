import firebase_admin
from firebase_admin import credentials, firestore
import os
import datetime

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
    firebase_admin.initialize_app(cred)

db = firestore.client()

def log_rating(user, song_title, rating, comment_id):
    """Store a user rating for a given song"""
    try:
        normalized_title = song_title.strip().lower()
        db.collection("ratings").add({
            "user": user,
            "song": normalized_title,
            "rating": rating,
            "comment_id": comment_id,
            "timestamp": datetime.datetime.utcnow()
        })
    except Exception as e:
        print(f"[Firestore Error] Failed to log rating: {e}")

def get_average_rating(song_title):
    """Retrieve average rating and count for a given song"""
    normalized_title = song_title.strip().lower()
    ratings_ref = db.collection("ratings").where("song", "==", normalized_title)
    docs = ratings_ref.stream()
    ratings = [doc.to_dict().get("rating", 0) for doc in docs]

    if ratings:
        avg = sum(ratings) / len(ratings)
        return round(avg, 2), len(ratings)

    return None, 0