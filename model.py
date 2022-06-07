from get_data import all_model_data, get_model_requirements
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors



def recommender_system(movie:str):
    
    output_prods = all_model_data(movie)

    return output_prods


def recommender_system_3(user_id:int, movie_name:str,n_similar_users:int, n_movies:int):
    refined_dataset,knn_model_user,knn_model_item,movies_df, movies_list,movie_dict = get_model_requirements()
    movies_seen = list(refined_dataset[refined_dataset['userId'] == user_id]['title'])

    def get_similar_users(user, n = 5):
        knn_input = np.asarray([user_to_movie_df.values[user-1]])
        distances, indices = knn_model_user.kneighbors(knn_input, n_neighbors=n+1)
        return indices.flatten()[1:] + 1, distances.flatten()[1:]
    
    
    def recommend_userbased():
         #Outputs indices of movies as rated by similar users
        similar_users_movies_indices = np.argsort(mean_rating_list)[::-1]
        similar_user_movie_names = movies_df[movies_df['movieId'].isin(similar_users_movies_indices)]['title'].values
        return similar_user_movie_names

    def get_similar_movies(movie, n = 10):
        # Outputs the movies similar to the given movie name.
        # rating_pivot_whole =  refined_dataset.pivot(index='title',columns='userId',values='rating').fillna(0)
        index = movie_dict[movie]
        knn_input = np.asarray([ratings_pivot.values[index]])

        n = min(len(movies_list)-1,n)
        distances, indices = knn_model_item.kneighbors(knn_input, n_neighbors=n+1)
        recommended_list =[]
        for i in range(1,len(distances[0])):
            recommended_list.append(movies_list[indices[0][i]])
        return recommended_list
    
    
    ratings_pivot = refined_dataset.pivot(index='title',columns='userId',values='rating').fillna(0)
    user_to_movie_df = refined_dataset.pivot(index='userId',columns='title',values='rating').fillna(0)
    similar_users, distances = get_similar_users(user_id,n_similar_users)
    weightage_list = distances/np.sum(distances)
    similar_users_ratings = user_to_movie_df.values[similar_users]
    weightage_list = weightage_list[:,np.newaxis] + np.zeros(ratings_pivot.shape[0])
    new_rating_matrix = weightage_list*similar_users_ratings
    mean_rating_list = new_rating_matrix.sum(axis =0)
    similar_users_movies = recommend_userbased()
    # Filtering out the movies already seen by user
    filtered_similar_movies = [i for i in similar_users_movies if i not in movies_seen]
    recommended_list =  get_similar_movies(movie_name)
    final_list = [i for i in recommended_list if i in filtered_similar_movies]
    if len(final_list)<n_movies:
        return final_list
    return final_list[:n_movies]