# Movie-Recommendations
link to dataset: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=ratings.csv (download ratings and movies_metadata)

The purpose of this project is to build a movie recommendation system using the Movies dataset, which contains ratings and metadata for over 45,000 movies.

To build the recommendation system, we first loaded the ratings data into a pandas DataFrame and split it into training and testing sets. We then used the Surprise library to create a recommendation model based on singular value decomposition (SVD), and evaluated its performance using the root mean squared error (RMSE).

We also loaded the movie data into a pandas DataFrame and defined a function to recommend movies to a user based on their predicted ratings. The function takes a user ID and the number of recommendations to return as input, and returns a list of recommended movies sorted by their predicted ratings.

This movie recommendation system is useful to someone who wants to quickly and easily discover new movies that they may enjoy based on their previous ratings and preferences. By providing personalized recommendations, this system can help users find movies that they might not have otherwise discovered, leading to a more enjoyable and fulfilling movie-watching experience.
