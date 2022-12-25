import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

def recommend_book(book):
    index = books[books['title'] == book].index[0]
    distances = sorted(list(enumerate(books_similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_books = []
    recommended_books_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        #movie_id = movies.iloc[i[0]].id
        recommended_books_posters.append(books.iloc[i[0]]['coverImg'])
        recommended_books.append(books.iloc[i[0]]['title'])

    return recommended_books, recommended_books_posters


def recommend_show(show):
    index = shows[shows['Series_Title'] == show].index[0]
    distances = sorted(list(enumerate(shows_similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_shows = []
    recommended_shows_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        #movie_id = movies.iloc[i[0]].id
        recommended_shows_posters.append(shows.iloc[i[0]]['Poster_Link'])
        recommended_shows.append(shows.iloc[i[0]]['Series_Title'])

    return recommended_shows, recommended_shows_posters



st.header('Entertainment Recommender System')
movies = pd.DataFrame(pickle.load(open('model/movie_dict.pkl','rb')))
similarity = pickle.load(open('model/similarity.pkl','rb'))
books = pd.DataFrame(pickle.load(open('model/books_dict.pkl','rb')))
books_similarity = pickle.load(open('model/books_similarity.pkl','rb'))
shows = pd.DataFrame(pickle.load(open('model/shows_dict.pkl','rb')))
shows_similarity = pickle.load(open('model/shows_similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Movie Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

book_list = books['title'].values
selected_books = st.selectbox(
    "Type or select a Book from the dropdown",
    book_list
)

if st.button('Show Book Recommendation'):
    recommended_books, recommended_books_posters = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[0])
        st.image(recommended_books_posters[0])
    with col2:
        st.text(recommended_books[1])
        st.image(recommended_books_posters[1])

    with col3:
        st.text(recommended_books[2])
        st.image(recommended_books_posters[2])
    with col4:
        st.text(recommended_books[3])
        st.image(recommended_books_posters[3])
    with col5:
        st.text(recommended_books[4])
        st.image(recommended_books_posters[4])


show_list = shows['Series_Title'].values
selected_shows = st.selectbox(
    "Type or select a TV show from the dropdown",
    show_list
)

if st.button('Show Shows Recommendation'):
    recommended_shows, recommended_shows_posters = recommend_show(selected_shows)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_shows[0])
        st.image(recommended_shows_posters[0])
    with col2:
        st.text(recommended_shows[1])
        st.image(recommended_shows_posters[1])

    with col3:
        st.text(recommended_shows[2])
        st.image(recommended_shows_posters[2])
    with col4:
        st.text(recommended_shows[3])
        st.image(recommended_shows_posters[3])
    with col5:
        st.text(recommended_shows[4])
        st.image(recommended_shows_posters[4])
