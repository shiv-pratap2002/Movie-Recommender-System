import requests
import streamlit as st
import json

# defines an h1 header
st.title("Recommender System")

# displays a file uploader widget

userid = st.text_input('User ID')
moviename = st.text_input('Movie Name')
n_users = st.text_input('Number of similar users to consider -')
n_movies = st.text_input('Enter number of movies to recommend')
data = {
    'userid': userid,
    'moviename':moviename,
    'n_similar_users': n_users,
    'n_movies':n_movies
}
if st.button("Make Recommendations"):
    res = requests.post(f"http://127.0.0.1:8000/recommend_3", json=data)
    show = json.loads(res.text)
    st.markdown('Following Movies are recommended : ')
    for i in show:
        st.write(i)
