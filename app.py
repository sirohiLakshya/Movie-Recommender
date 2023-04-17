import base64
import pandas as pd
import streamlit as st
import pickle
import requests
import numpy as np

#Keeping the layout as wide by default

st.set_page_config(  
    layout="wide", 
    page_icon=None,
    page_title='Movie Recommender'
)

#Setting the distance between the top of the page and the heading 
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

#Setting the background image for the page

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
        return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('bgf.png')

#Making a function to get the poster path from a movie id and it will send a request to the TMDB for the poster, 
#for sending such requests we need requests library to be imported

def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=e5f3fe1800d0213d15ceb23bf41d67ae&language=en-US'.format(
            movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

#Making a function to get the recommended movies name and posters

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # Getting the index of the movies
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching the poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

#To get the the movie title from the movie dictionary file
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

#Making a function to get the cosine similarity values from our ML model through the similarity.pkl file
similarity = pickle.load(open('similarity.pkl', 'rb'))

#Setting the title for the first search bar
st.title('Movie Recommender')

#Making a text box to take input from user
selected_movie_name = st.selectbox('Movies similar to:', movies['title'].values)

#Making a button for user to get the recommendations
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    #to display the movie names and posters
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.text(names[5])
        st.image(posters[5])

    with col7:
        st.text(names[6])
        st.image(posters[6])

    with col8:
        st.text(names[7])
        st.image(posters[7])

    with col9:
        st.text(names[8])
        st.image(posters[8])

    with col10:
        st.text(names[9])
        st.image(posters[9])

#To set the title for the 2nd search bar
st.title('Know Your Next Movie')
title = st.text_input("Type the title and press Enter")
if title:
    try:
        #sending request to omdb for getting movie details
        url = f"http://www.omdbapi.com/?t={title}&apikey=d6782a35"
        re = requests.get(url)
        re = re.json()
        #To display the poster and other relevant details of the movie 
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(re['Poster'])
        with col2:
            st.subheader(re['Title'])
            st.caption(f"Genre:{re['Genre']}")
            st.write(f"Release Date: {re['Released']}")
            st.write(f"Rated: {re['Rated']}")
            st.write(f"Plot: {re['Plot']}")
            st.write(f"Cast: {re['Actors']}")
            st.text(f"IMDb Rating: {re['imdbRating']}")
            st.progress(float(re['imdbRating']) / 10)
            st.text(f"Metacritic Rating: {re['Metascore']}")
            st.progress(float(re['Metascore']) / 100)

    except:
        st.error('No movie found or some data missing!') 
