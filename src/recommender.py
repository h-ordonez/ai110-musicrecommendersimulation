import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_danceability: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

FLOAT_FIELDS = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")

W_GENRE = 2.0
W_MOOD = 1.5
W_VALENCE = 1.3
W_TEMPO = 1.2
W_ENERGY = 1.0
W_DANCE = 1.0
W_ACOUSTIC = 0.8
TOTAL_WEIGHT = W_GENRE + W_MOOD + W_VALENCE + W_TEMPO + W_ENERGY + W_DANCE + W_ACOUSTIC

MAX_TEMPO_DIFF = 60
CLOSE_ENOUGH = 0.8

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts with numeric fields cast to int/float."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        songs = []
        for row in reader:
            row["id"] = int(row["id"])
            for field in FLOAT_FIELDS:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences using the weighted feature-closeness recipe, returning (score, reasons)."""
    genre_score = 1.0 if song["genre"] == user_prefs["genre"] else 0.0
    mood_score = 1.0 if song["mood"] == user_prefs["mood"] else 0.0
    energy_score = 1 - abs(song["energy"] - user_prefs["energy"])
    dance_score = 1 - abs(song["danceability"] - user_prefs["danceability"])
    valence_score = 1 - abs(song["valence"] - user_prefs["valence"])
    acoustic_score = 1 - abs(song["acousticness"] - user_prefs["acousticness"])
    tempo_score = 1 - min(abs(song["tempo_bpm"] - user_prefs["tempo_bpm"]) / MAX_TEMPO_DIFF, 1.0)

    total_score = (
        W_GENRE * genre_score
        + W_MOOD * mood_score
        + W_VALENCE * valence_score
        + W_TEMPO * tempo_score
        + W_ENERGY * energy_score
        + W_DANCE * dance_score
        + W_ACOUSTIC * acoustic_score
    ) / TOTAL_WEIGHT

    reasons = []
    if genre_score == 1.0:
        reasons.append(f"Matches favorite genre '{song['genre']}'")
    if mood_score == 1.0:
        reasons.append(f"Matches favorite mood '{song['mood']}'")
    if energy_score >= CLOSE_ENOUGH:
        reasons.append(f"Energy close to target ({song['energy']:.2f} vs {user_prefs['energy']:.2f})")
    if dance_score >= CLOSE_ENOUGH:
        reasons.append(f"Danceability close to target ({song['danceability']:.2f} vs {user_prefs['danceability']:.2f})")
    if valence_score >= CLOSE_ENOUGH:
        reasons.append(f"Valence close to target ({song['valence']:.2f} vs {user_prefs['valence']:.2f})")
    if acoustic_score >= CLOSE_ENOUGH:
        reasons.append(f"Acousticness close to target ({song['acousticness']:.2f} vs {user_prefs['acousticness']:.2f})")
    if tempo_score >= CLOSE_ENOUGH:
        reasons.append(f"Tempo close to target ({song['tempo_bpm']:.0f} vs {user_prefs['tempo_bpm']:.0f} bpm)")

    return total_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, rank by score descending, and return the top k as (song, score, explanation) tuples."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    scored.sort(key=lambda entry: entry[1], reverse=True)
    return [(song, score, "; ".join(reasons)) for song, score, reasons in scored[:k]]
