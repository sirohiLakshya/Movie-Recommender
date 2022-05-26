import base64
import pandas as pd
import streamlit as st
import pickle
import requests

st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    page_icon=None,  # String, anything supported by st.image, or None.
    page_title='Movie Recommender'

)

st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)


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


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=e5f3fe1800d0213d15ceb23bf41d67ae&language=en-US'.format(
            movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


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


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender')

selected_movie_name = st.selectbox('Movies similar to:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
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
# st.markdown(
# """
# <style>
# .stProgress > div > div > div > div {
# background-color: #a76751;
# }
# </style>""",
# unsafe_allow_html=True,
# )

st.title('Know Your Next Movie')
title = st.text_input("Type the title and press Enter")
if title:
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey=d6782a35"
        re = requests.get(url)
        re = re.json()
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
