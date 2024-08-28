import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movies_id=i[0]
        #fetch poster from api

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl','rb'))

movies_list=movies_list['title'].values
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Which Movie',movies_list
)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)