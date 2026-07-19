# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Suggest A Song 1.0 

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender creates a user profile based on various user preferences and suggests songs based on these preferences. It assumes the user does not stray too far away from these preferences. This recommender is for classroom exploration and provides a way to experiment with how songs are recommended.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

This model works by considering all seven features of a song: genre, mood, energy, tempo_bpm, valence, danceability, acousticness. The same song features are considered for user preferences. The model turns the feature into a score by using weighted values for each feature. The weights for each feature vary, with genre having the heaviest weight and acousticness having the lightest. Genre and mood require an exact match and get a value of either 1 or 0, while energy, danceability, valence, tempo_bpm, and acousticness are normalized to a scale between 0 and 1. All features are combined into one total score. The songs are then sorted in descending order based on this total score.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset

There are a total of 20 songs in the catalog. The songs span a variety of genres and moods. To name a few, these include pop, rock, indie, folk, and edm, for genre; and happy, chill, intense, nostalgic, and romantic for mood. No data was removed, but 10 songs were added to the original set. A wide variety of genres are missing from the set.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system appears to give reasonable results for users who prefer pop music. This is because pop is the most common genre type in the data set. The system typically recommended songs from this genre to users who had pop listed as their favorite genre.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users

One limitation I observed had to with genre and mood not being decisive factors as I had previously expected. Claude created a user profile that should have had a rock song in its top 5 recommendations based on the user's favorite genre being rock, but the song did not appear at all. Moonlight Sonata Reprise was the top recommended song because the other numerical values aligned very closely with the user's preferences. It's also possible that there were not enough rock songs in the data set with matching numerical values that could have otherwise been pushed into the top five.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested high energy dance, moody acoustic, and punk rock profiles. In the recommendations I expected to see songs that closely aligned with user preferences based on genre primarily. However, I was often surprised to see that genre was not always a determining factor for the top song that was suggested. Oftentimes, songs that I did not expect to be at the top were there. This was indicative that I may not have put enough weight on genre, so I tried increasing the weight which generally helped.

When comparing profiles, high energy dance profiles preferred high danceability songs with low acousticness, as opposed to moody acoustic profiles preferring high acousticness songs with low danceability. 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

The main improvement to be made for this model is dramatically increasing the number of songs in the data set. This will provide more song recommendations that align with a user's preferences based on genre. Furthermore, the model should nalso be able to handle sub-genres of music, as these are currently treated as discrete genres (e.g., punk rock and heavy metal are sub-genres of rock). This would provide users who prefer a general genre a way of being recommended sub-genres that might score well in other metrics such as mood, energy, etc.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommender systems are very complex. It is difficult to pinpoint which metrics matter the most because not all users place the same importance on the same metrics. For example, one user may be very rigid in the genre of music she likes, but another user may not care as much about genre as they do about energy. I found this to be interesting because it could mean that apps like Spotify might require a more dynamic approach to how they recommend music. There is no one-size-fits-all when it comes to musical preferences, and so I would expect the same when it comes to recommender algorithms.
