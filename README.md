# Recommender System

This is a repo containing my 4th Semester ML mini-project submission
## Dataset
The popular MovieLens100k Dataset is used for this project which contains 100k ratings collected from 1k users on 1700 movies, each user has rated at least 20 movies on a scale of 1 to 5.


This Project has 3 components - 

#### 1 - Recommender System made using movielens dataset using sklearn.
  - What this system basically does is it computes user-to-user similarities and item-to-item similarities using collaborative filtering
  - Given an input userId it collects all the movies that similar users have watched, ranked by the ranking metric of dataset
  - Then given an input Movie Name, it uses the item-based similarity to output the similar movies to this movie from the collection we got earlier.
  - The system makes sure the final movie set that's to be recommended to the user doesn't contain the movies they have already watched.

#### 2 - API linking the model code with the Streamlit UI 
  - FastAPI was used to develop a very simple API to link the model with Streamlit UI

#### 3 - Streamlit UI
  - A very basic Streamlit UI to basically take inputs and show outputs.


## Future Ideas
Since this miniproject was developed by me under tight time contraints, I feel it lacks few features that can be added given some time, I hope to develop a far more efficient Recommender System adding a content-based component in the mix as the Hybrid-Recommender System as approach overcomes the limitations of both content-based and collaborative filtering methods. Also, the UI can use some major overhaul to make this project visually appealing.
