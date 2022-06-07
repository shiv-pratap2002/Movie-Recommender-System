import pickle
import pandas as pd

def all_model_data(movie: str):
    recommendations_file = open('prestructuring-results.pickle', 'rb')
    dictionary = pickle.load(recommendations_file)
    recommendations_file.close()
    
    return dictionary[movie]

def get_model_requirements():
    refined_df = pd.read_pickle('refined_dataset.pickle')
    knn_model_user_file = open('user_to_user_model.pickle', 'rb')
    knn_model_user = pickle.load(knn_model_user_file)
    knn_model_user_file.close()
    knn_model_item_file = open('item_to_item_model.pickle', 'rb')
    knn_model_item = pickle.load(knn_model_item_file)
    knn_model_item_file.close()
    movies_df = pd.read_pickle('movie_df.pickle')
    movie_list_file = open('movies_list.pickle', 'rb')
    movie_list = pickle.load(movie_list_file)
    movie_list_file.close()
    movie_dict_file = open('movies_dict.pickle', 'rb')
    movie_dict = pickle.load(movie_dict_file)
    movie_dict_file.close()
    # d = {'refined_df':refined_df,'knn_model_user':knn_model_item}
    
    return refined_df,knn_model_user,knn_model_item,movies_df, movie_list,movie_dict