"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import textwrap

from src.recommender import load_songs, recommend_songs

RANK_WIDTH = 5
TITLE_WIDTH = 25
SCORE_WIDTH = 8
EXPLANATION_WIDTH = 50


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs from data/songs.csv")

    # Starter example profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "danceability": 0.8,
        "valence": 0.8,
        "tempo_bpm": 120,
        "acousticness": 0.2,
    }
    print(f"User preferences: {user_prefs}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    indent = " " * (RANK_WIDTH + TITLE_WIDTH + SCORE_WIDTH)
    header = f"{'Rank':<{RANK_WIDTH}}{'Title':<{TITLE_WIDTH}}{'Score':<{SCORE_WIDTH}}{'Explanation'}"
    print(header)
    print("-" * len(header))
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        wrapped_lines = textwrap.wrap(explanation, width=EXPLANATION_WIDTH) or [""]
        print(f"{rank:<{RANK_WIDTH}}{song['title']:<{TITLE_WIDTH}}{score:<{SCORE_WIDTH}.2f}{wrapped_lines[0]}")
        for line in wrapped_lines[1:]:
            print(f"{indent}{line}")


if __name__ == "__main__":
    main()
