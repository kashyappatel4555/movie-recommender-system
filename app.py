import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Fetch movie poster from TMDb API
def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": api_key,
        "language": "en-US"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path
        else:
            return "Poster not available"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return None

# Recommendation function
def recommend_movies(movie):
    if movie not in movies['title'].values:
        return ["Movie not found. Please check the spelling or try a different movie."], []
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

st.title('Movie Recommender System')
selected_movie = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend_movies(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
