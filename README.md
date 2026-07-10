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

My system uses genre, mood, energy, and danceability. The reason I decided to go with these attributes is because genre and mood are typical indicators for me of whether or not I will like a song. Energy and danceability are important because they offer a numerical value that can be used to gauge a user's preference. As such, UserProfile will store these four values since they are the core of my music recommender. In addition, my recommender will compute a score for each song based on a simple distance-based similarity score: score_energy = 1 - |song.energy - user.target_energy|. The songs that are recommended will be based on a weighted-sum formula where genre is weighted heaviest and mood is weighted second heaviest. For example, if a genre matches a user's favorite genre, then it is more likely to be recommended than a song that does not match the genre but hits other metrics.

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
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



