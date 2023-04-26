import pandas as pd

# Load the movie data into a pandas DataFrame
movies_df = pd.read_csv('movies_metadata.csv')


# Define a function to recommend movies to a user
def recommend_movies(user_preferences):
    # Create a copy of the movies DataFrame
    recommendations_df = movies_df.copy()

    # Filter the DataFrame to include only movies that match the user's preferences
    for preference in user_preferences:
        recommendations_df = recommendations_df[recommendations_df[preference[0]] == preference[1]]

    # Sort the DataFrame by the user's preferred metric (e.g. rating, release date)
    recommendations_df.sort_values(by=user_preferences[-1][0], ascending=False, inplace=True)

    # Return the top 10 recommendations
    return recommendations_df.head(10)


# Example usage
user_preferences = [('genre', 'Action'), ('year', 2010), ('rating', 'PG-13')]
recommendations= recommend_movies(user_preferences)
print(recommendations)
