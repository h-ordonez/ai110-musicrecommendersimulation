# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
  
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

My understanding of how other streaming services make recommendations is that they use collaborative filtering or content-based filtering. In collaborative filtering, the service finds a group of people who have similar tastes, and recommends content to one user based on what the other people in the same group liked. In content-based filtering, the service identifies key metrics of the content itself that a given user prefers, and makes recommendations based on other content with similar metrics. In general, many streaming services use a hybrid approach. My music recommender will proritize content-based filtering. 

My system uses genre, mood, energy, danceability, and likes_acoustic. The reason I decided to go with these attributes is because genre and mood are typical indicators for me of whether or not I will like a song. Energy and danceability are important because they offer a numerical value that can be used to gauge a user's preference. As such, UserProfile will store these four values since they are the core of my music recommender. In addition, my recommender will compute a score for each song based on a simple distance-based similarity score: score_energy = 1 - |song.energy - user.target_energy|. The songs that are recommended will be based on a weighted-sum formula where genre is weighted heaviest and mood is weighted second heaviest. For example, if a genre matches a user's favorite genre, then it is more likely to be recommended than a song that does not match the genre but hits other metrics.

### Algorithm Recipe

1. Pre-feature scoring: every song gets scored feature-by-feature (e.g., genre, mood, energy, etc.).

2. Weighted combination: the song's features are combined into one total score via weighted sum, then divided by the sum of the weights so the result stays in the range [0, 1].

3. Explanation to user: Each feature that scores well will get appended to a message that is later given to the user as the reason why a song was recommended.

4. Ranking: Songs are sorted into descending order so that the top k songs may be taken.

One note on potential biases is that the recommender is very likely to skew towards genres the user likes, and not really favor songs that are danceable or be acoustic. This can be a problem particularly for users who have a diverse taste in music.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded 20 songs from data/songs.csv
User preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8, 'danceability': 0.8, 'valence': 0.8, 'tempo_bpm': 120, 'acousticness': 0.2}

Top recommendations:

Rank Title                    Score   Explanation
-------------------------------------------------
1    Sunrise City             0.98    Matches favorite genre 'pop'; Matches favorite
                                      mood 'happy'; Energy close to target (0.82 vs
                                      0.80); Danceability close to target (0.79 vs
                                      0.80); Valence close to target (0.84 vs 0.80);
                                      Acousticness close to target (0.18 vs 0.20); Tempo
                                      close to target (118 vs 120 bpm)
2    Gym Hero                 0.76    Matches favorite genre 'pop'; Energy close to
                                      target (0.93 vs 0.80); Danceability close to
                                      target (0.88 vs 0.80); Valence close to target
                                      (0.77 vs 0.80); Acousticness close to target (0.05
                                      vs 0.20); Tempo close to target (132 vs 120 bpm)
3    Rooftop Lights           0.74    Matches favorite mood 'happy'; Energy close to
                                      target (0.76 vs 0.80); Danceability close to
                                      target (0.82 vs 0.80); Valence close to target
                                      (0.81 vs 0.80); Acousticness close to target (0.35
                                      vs 0.20); Tempo close to target (124 vs 120 bpm)
4    Pulse Overdrive          0.55    Energy close to target (0.90 vs 0.80);
                                      Danceability close to target (0.90 vs 0.80);
                                      Valence close to target (0.80 vs 0.80);
                                      Acousticness close to target (0.05 vs 0.20); Tempo
                                      close to target (128 vs 120 bpm)
5    Night Drive Loop         0.52    Energy close to target (0.75 vs 0.80);
                                      Danceability close to target (0.73 vs 0.80);
                                      Acousticness close to target (0.22 vs 0.20); Tempo
                                      close to target (110 vs 120 bpm)
```

### Recommendations for different profiles
```
High energy dance
Preferences: {'genre': 'electronic', 'mood': 'energetic', 'energy': 0.9, 'danceability': 0.9, 'valence': 0.7, 'tempo_bpm': 130, 'acousticness': 0.1}

Top recommendations:

Rank Title                    Score   Explanation
-------------------------------------------------
1    Pulse Overdrive          0.75    Matches favorite mood 'energetic'; Energy close to
                                      target (0.90 vs 0.90); Danceability close to
                                      target (0.90 vs 0.90); Valence close to target
                                      (0.80 vs 0.70); Acousticness close to target (0.05
                                      vs 0.10); Tempo close to target (128 vs 130 bpm)
2    Gym Hero                 0.58    Energy close to target (0.93 vs 0.90);
                                      Danceability close to target (0.88 vs 0.90);
                                      Valence close to target (0.77 vs 0.70);
                                      Acousticness close to target (0.05 vs 0.10); Tempo
                                      close to target (132 vs 130 bpm)
3    Sunrise City             0.53    Energy close to target (0.82 vs 0.90);
                                      Danceability close to target (0.79 vs 0.90);
                                      Valence close to target (0.84 vs 0.70);
                                      Acousticness close to target (0.18 vs 0.10); Tempo
                                      close to target (118 vs 130 bpm)
4    Rooftop Lights           0.52    Energy close to target (0.76 vs 0.90);
                                      Danceability close to target (0.82 vs 0.90);
                                      Valence close to target (0.81 vs 0.70); Tempo
                                      close to target (124 vs 130 bpm)
5    Storm Runner             0.49    Energy close to target (0.91 vs 0.90);
                                      Acousticness close to target (0.10 vs 0.10
```

```
Moody acoustic
Preferences: {'genre': 'indie', 'mood': 'moody', 'energy': 0.3, 'danceability': 0.2, 'valence': 0.5, 'tempo_bpm': 110, 'acousticness': 0.8}

Top recommendations:

Rank Title                    Score   Explanation
-------------------------------------------------
1    Night Drive Loop         0.61    Matches favorite mood 'moody'; Valence close to
                                      target (0.49 vs 0.50); Tempo close to target (110
                                      vs 110 bpm)
2    Moonlight Sonata Reprise 0.48    Energy close to target (0.25 vs 0.30);
                                      Danceability close to target (0.20 vs 0.20);
                                      Valence close to target (0.55 vs 0.50);
                                      Acousticness close to target (0.95 vs 0.80)
3    Autumn Fields            0.48    Energy close to target (0.33 vs 0.30); Valence
                                      close to target (0.62 vs 0.50); Acousticness close
                                      to target (0.80 vs 0.80)
4    Dirt Road Home           0.47    Energy close to target (0.50 vs 0.30); Valence
                                      close to target (0.68 vs 0.50); Tempo close to
                                      target (100 vs 110 bpm)
5    Coffee Shop Stories      0.47    Energy close to target (0.37 vs 0.30);
                                      Acousticness close to target (0.89 vs 0.80)
```

```
ADVERSARIAL: genre/mood trap
Preferences: {'genre': 'rock', 'mood': 'happy', 'energy': 0.25, 'danceability': 0.2, 'valence': 0.55, 'tempo_bpm': 66, 'acousticness': 0.95}

Top recommendations:

Rank Title                    Score   Explanation
-------------------------------------------------
1    Moonlight Sonata Reprise 0.60    Energy close to target (0.25 vs 0.25);
                                      Danceability close to target (0.20 vs 0.20);
                                      Valence close to target (0.55 vs 0.55);
                                      Acousticness close to target (0.95 vs 0.95); Tempo
                                      close to target (66 vs 66 bpm)
2    Spacewalk Thoughts       0.54    Energy close to target (0.28 vs 0.25); Valence
                                      close to target (0.65 vs 0.55); Acousticness close
                                      to target (0.92 vs 0.95); Tempo close to target
                                      (60 vs 66 bpm)
3    Library Rain             0.52    Energy close to target (0.35 vs 0.25); Valence
                                      close to target (0.60 vs 0.55); Acousticness close
                                      to target (0.86 vs 0.95); Tempo close to target
                                      (72 vs 66 bpm)
4    Autumn Fields            0.52    Energy close to target (0.33 vs 0.25); Valence
                                      close to target (0.62 vs 0.55); Acousticness close
                                      to target (0.80 vs 0.95); Tempo close to target
                                      (76 vs 66 bpm)
5    Backroad Blues           0.50    Energy close to target (0.40 vs 0.25); Valence
                                      close to target (0.42 vs 0.55); Tempo close to
                                      target (70 vs 66 bpm)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I did an experiment where I omitted the mood of a song. This had surprising results. For example, the song rankings for the punk rock profile resulted in a punk rock song scoring lower than it had before. This showed that mood was doing a lot of heavy lifting for this type of user. However, in other profiles where other values were close to the target value for the user, mood did not have a significant impact.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

The biggest limitation of the recommender is the small data set. This is because it tends to give a greater priority to genre and mood, and when there aren't enough songs that match this criteria, there are surprising song recommendations.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

Recommenders turn data into predictions by looking at the type of content a user consumes, or the type of a content a user deliberately says they like. This data is then fed into a mathematical formula that is fine-tuned to match a user's preferences with content that matches those preferences in the system's catalog.

This can lead to bias or unfairness because large populations of people are inherently unpredictable. For instance, there are no laws in nature that state a fan of heavy metal music will not like classical music or hip-hop, and so this means that a recommender is working with a very narrow understanding of its users. Therefore, it is imperative that developers of these recommenders be aware of biases and have gaurdrails built into them to minimize poor results.



