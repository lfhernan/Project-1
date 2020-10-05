'''
Name: Luis F. Hernandez JR
PID: 5163353
Class: COP 4813 Web Application Programming
Assignment: Project 1 - Streamlit, NYTimes API, JSON Documents
'''

import streamlit as st
import main_functions

topic_options = ["", "arts", "automobiles", "books", "business", "fashion", "food", "health", "home",
                 "insider", "magazine", "movies", "nyregion", "obituaries", "opinion", "politics",
                 "realestate", "science", "sports", "sundayreview", "technology", "theater", "t-magazine",
                 "travel", "upshot", "us", "world"]

article_types = ["", "shared", "emailed", "viewed"]

article_times = ["", "1", "7", "30"]

st.title("COP 4813 - Web Application Programming")
st.header("Project 1")
st.subheader("Part A - Top Stories API")

st.write("Please enter your name")
name = st.text_input(label="Name")
st.write("Please select a topic")
topic = st.selectbox(label="Topic", options=topic_options)

if name and topic:
    st.write("Hello " + name + "! You've selected the " + topic + " topic.")
    freqDist = st.checkbox(label="Click here to see frequency distribution of the 10 most common words in your topic")

    if freqDist:
        word_dist = main_functions.freq_dist(topic)
        fig = main_functions.create_figure(word_dist)
        st.pyplot(fig)

    word_cloud = st.checkbox(label="Click here to generate a word cloud")

    if word_cloud:
        main_functions.create_wordcloud_top_stories(topic)
        st.image("top_articles_wordcloud.png", caption="Wordcloud of the most common words in the " + topic + " topic.", use_column_width=True)

st.subheader("Part B - Most Popular API")

st.write("Please select if you would like to see the most shared, emailed, or viewed articles")
article = st.selectbox(label="Preferred set of articles", options=article_types)

st.write("Please select the time period of the most popular articles (1, 7, or 30 days)")
times = st.selectbox(label="Time Period (days)", options=article_times)

if article and times:
    main_functions.create_wordcloud_most_popular(article, times)
    st.image("most_popular_wordcloud.png", caption="Wordcloud of " + article + " articles", use_column_width=True)