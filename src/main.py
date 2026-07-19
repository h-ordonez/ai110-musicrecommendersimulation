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

    # Three distinct example prefs for testing
    high_energy_dance_prefs = {
        "genre": "electronic",
        "mood": "energetic",
        "energy": 0.9,
        "danceability": 0.9,
        "valence": 0.7,
        "tempo_bpm": 130,
        "acousticness": 0.1,
    }

    moody_acoustic_prefs = {
        "genre": "indie",
        "mood": "moody",
        "energy": 0.3,
        "danceability": 0.2,
        "valence": 0.5,
        "tempo_bpm": 110,
        "acousticness": 0.8,
    }

    punk_rock_prefs = {
        "genre": "rock",
        "mood": "angry",
        "energy": 0.8,
        "danceability": 0.5,
        "valence": 0.4,
        "tempo_bpm": 140,
        "acousticness": 0.2,
    }

    # --- Adversarial / edge-case profiles for stress testing ---

    # Numeric-perfect but genre/mood totally wrong. Targets Moonlight Sonata
    # Reprise's exact numeric attributes (classical/calm) while asking for
    # rock/happy -- tests whether genre/mood actually "gate" as claimed.
    genre_mood_trap_prefs = {
        "genre": "rock",
        "mood": "happy",
        "energy": 0.25,
        "danceability": 0.20,
        "valence": 0.55,
        "tempo_bpm": 66,
        "acousticness": 0.95,
    }

    # Case-sensitivity trap: "pop"/"happy" exist verbatim in the data, but
    # exact-match is case-sensitive -- expect genre_score/mood_score = 0.
    case_sensitivity_trap_prefs = {
        "genre": "Pop",
        "mood": "Happy",
        "energy": 0.8,
        "danceability": 0.8,
        "valence": 0.8,
        "tempo_bpm": 120,
        "acousticness": 0.2,
    }

    # Substring/compound-genre trap: a human would call "punk rock" and
    # "heavy metal" variants of "rock", but exact-match means "rock" only
    # matches Storm Runner.
    compound_genre_trap_prefs = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "danceability": 0.6,
        "valence": 0.4,
        "tempo_bpm": 160,
        "acousticness": 0.08,
    }

    # Out-of-range / bad-input trap: simulates a UI bug or a user typing on a
    # 0-10 scale instead of 0-1. No input validation exists, so this silently
    # produces negative feature scores instead of erroring or clamping.
    out_of_range_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 8.0,  # should be 0.8
        "danceability": 0.8,
        "valence": 0.8,
        "tempo_bpm": 120,
        "acousticness": 0.2,
    }

    # Extreme-tempo trap: tempo_score is clamped at 0 via min(..., 1.0), but
    # energy/valence/dance/acoustic are NOT. This isolates that inconsistency.
    extreme_tempo_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "danceability": 0.8,
        "valence": 0.8,
        "tempo_bpm": 1000,
        "acousticness": 0.2,
    }

    # Nonexistent genre+mood combo: no song is "electronic"/"energetic"
    # exactly (closest is genre="edm"), so this degrades to a pure numeric
    # contest -- worth checking whether the system still confidently returns
    # a top-5 with no signal that nothing actually matches taste.
    no_genre_match_prefs = {
        "genre": "electronic",
        "mood": "energetic",
        "energy": 0.9,
        "danceability": 0.9,
        "valence": 0.9,
        "tempo_bpm": 128,
        "acousticness": 0.05,
    }

    profiles = [
        ("Starter (pop/happy)", user_prefs),
        ("High energy dance", high_energy_dance_prefs),
        ("Moody acoustic", moody_acoustic_prefs),
        ("Punk rock", punk_rock_prefs),
        ("ADVERSARIAL: genre/mood trap", genre_mood_trap_prefs),
        ("ADVERSARIAL: case sensitivity trap", case_sensitivity_trap_prefs),
        ("ADVERSARIAL: compound genre trap", compound_genre_trap_prefs),
        ("ADVERSARIAL: out-of-range input", out_of_range_prefs),
        ("ADVERSARIAL: extreme tempo", extreme_tempo_prefs),
        ("ADVERSARIAL: no genre/mood match", no_genre_match_prefs),
    ]

    for label, prefs in profiles:
        print(f"\n{'=' * 70}")
        print(f"{label}")
        print(f"Preferences: {prefs}")
        print_recommendations(prefs, songs, k=5)

    # Boundary check: k larger than the song list should not crash.
    print(f"\n{'=' * 70}")
    print("BOUNDARY: k=100 (larger than song list)")
    overflow_results = recommend_songs(user_prefs, songs, k=100)
    print(f"Requested k=100, got {len(overflow_results)} results (song list has {len(songs)})")


def print_recommendations(user_prefs, songs, k=5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)

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
