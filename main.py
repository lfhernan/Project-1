'''
Luis F. Hernandez JR
5163353
'''

import streamlit as st
import main_functions

topic_options = ["", "arts", "automobiles", "books", "business", "fashion", "food", "health", "home",
                 "insider", "magazine", "movies", "nyregion", "obituaries", "opinion", "politics",
                 "realestate", "science", "sports", "sundayreview", "technology", "theater", "t-magazine",
                 "travel", "upshot", "us", "world"]

st.title("COP 4813 - Web Application Programming")
st.header("Project 1")
st.subheader("Part A - Top Stories API")

st.write("Please enter your name")
name = st.text_input(label="Name")
st.write("Please select a topic")
topic = st.selectbox(label="Topic", options=topic_options)

if name and topic:
    st.write("Hello " + name + "! You've selected the " + topic + " topic.")
    freqDist = st.checkbox(label="Click here to see frequency distribution of the 10 most common words")

    if freqDist:
        word_dist = main_functions.freq_dist(topic)
        fig = main_functions.create_figure(word_dist)
        st.pyplot(fig)

    word_cloud = st.checkbox(label="Click here to generate a word cloud")

    if word_cloud:
        main_functions.create_wordcloud(topic)
        st.image("Images/wordcloud.png", caption="Wordcloud of most common words", use_column_width=True)