'''
Luis F. Hernandez JR
5163353
'''

import streamlit as st
import pandas as pd
import numpy as np
from typing import List

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
        my_wordcloud = main_functions.create_wordcloud(topic)
        st.pyplot(my_wordcloud)

# nltk.download("punkt")
# nltk.download("stopwords")

# api_key_dict = main_functions.read_from_file("JSON_Files/api_key.json")
# api_key = api_key_dict["my_key"]
#
# url = "https://api.nytimes.com/svc/topstories/v2/health.json?api-key=" + api_key
#
# response = requests.get(url).json()
#
# main_functions.save_to_file(response, "JSON_Files/response.json")
#
# my_articles = main_functions.read_from_file("JSON_Files/response.json")
#
# str1 = ""
#
# for i in my_articles["results"]:
#     str1 = str1 + i["abstract"]
#
# sentences = sent_tokenize(str1)
# words = word_tokenize(str1)
# words_no_punkt = []
# clean_words = []
#
# for w in words:
#     if w.isalpha():
#         words_no_punkt.append(w.lower())
#
# fdist = FreqDist(words_no_punkt)
# stopwords = stopwords.words("english")
#
# for w in words_no_punkt:
#     if w not in stopwords:
#         clean_words.append(w)
#
# fdist2 = FreqDist(clean_words)
# pprint(fdist2.most_common(10))
#
# my_wordcloud = WordCloud().generate(str1)
# plt.figure(figsize=(12, 12))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()
