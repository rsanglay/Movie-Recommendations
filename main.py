import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from surprise import SVD
from surprise import Dataset
from surprise import Reader

# Load the ratings data into a pandas DataFrame
ratings_df = pd.read_csv('ratings.csv')

# Split the data into training and testing sets
train_data, test_data = train_test_split(ratings_df, test_size=0.2)

# Use the Surprise library to create a recommendation model
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(train_data[['userId', 'movieId', 'rating']], reader)
algo = SVD()
algo.fit(data.build_full_trainset())

# Make predictions on the test set
test_predictions = algo.test(test_data[['userId', 'movieId', 'rating']].values)

# Calculate the root mean squared error (RMSE) of the predictions
test_rmse = mean_squared_error(test_predictions[:, 2], test_predictions[:, 3], squared=False)
print('Test RMSE:', test_rmse)

# Load the movie data into a pandas DataFrame
movies_df = pd.read_csv('movies.csv')


# Define a function to recommend movies to a user
def recommend_movies(user_id, num_recommendations):
    # Get a list of all movies the user has not rated
    user_movies = ratings_df[ratings_df['userId'] == user_id]['movieId']
    unrated_movies = movies_df[~movies_df['movieId'].isin(user_movies)]['movieId']

    # Create a DataFrame of predicted ratings for the unrated movies
    predictions = []
    for movie_id in unrated_movies:
        prediction = algo.predict(user_id, movie_id)
        predictions.append((movie_id, prediction.est))
    predictions_df = pd.DataFrame(predictions, columns=['movieId', 'predicted_rating'])

    # Sort the DataFrame by predicted rating and return the top recommendations
    recommendations_df = predictions_df.sort_values(by='predicted_rating', ascending=False).head(num_recommendations)
    recommended_movies = pd.merge(recommendations_df, movies_df, on='movieId', how='inner')

    return recommended_movies[['title', 'genres']]


# Example usage
user_id = 1
num_recommendations = 10
recommendations = recommend_movies(user_id, num_recommendations)
print(recommendations)
