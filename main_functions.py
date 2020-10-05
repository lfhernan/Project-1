'''
Name: Luis F. Hernandez JR
PID: 5163353
Class: COP 4813 Web Application Programming
Assignment: Project 1 - Streamlit, NYTimes API, JSON Documents
'''

import json
import requests

from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

'''
A helper function to save data as a JSON Document
'''
def save_to_file(data, filename):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file, indent = 2)

'''
A helper function to read data from a JSON Document and return the data as a dictionary
'''
def read_from_file(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
    return data

'''
A function that uses NYTimes Top Stories API to pull the top stories from a given topic
@param topic - the topic the user would like to query
@returns - the articles in JSON format
'''
def pull_api_top_stories(topic):
    api_key_dict = read_from_file("JSON_Files/api_key.json")
    api_key = api_key_dict["my_key"]

    url = "https://api.nytimes.com/svc/topstories/v2/" + topic + ".json?api-key=" + api_key

    response = requests.get(url).json()

    save_to_file(response, "JSON_Files/response.json")

    return read_from_file("JSON_Files/response.json")

'''
A function that uses NYTimes Most Popular API to retrieve the most popular articles based on views, shares, or emails from 
the last day, week, or month.
@param article_type - the most popular articles based on either views, shares, or emails
@param time_period - the most popular articles from the last day (1), week (7), or month (30)
@returns - the articles in JSON format
'''
def pull_api_most_popular(article_type, time_period):
    api_key_dict = read_from_file("JSON_Files/api_key.json")
    api_key = api_key_dict["my_key"]

    url = "https://api.nytimes.com/svc/mostpopular/v2/" + article_type + "/" + time_period + ".json?api-key=" + api_key

    response = requests.get(url).json()

    save_to_file(response, "JSON_Files/response.json")

    return read_from_file("JSON_Files/response.json")

'''
A helper function that retrieves all of the words in the article's abstract section
@param topic - the topic selected by the user
@returns - a list of words without stop words or punctuation marks
'''
def get_words(topic):
    my_article = pull_api_top_stories(topic)

    abstract_words = ""

    for i in my_article["results"]:
        abstract_words = abstract_words + i["abstract"]

    words = word_tokenize(abstract_words)

    words_no_punkt = []
    clean_words = []

    for w in words:
        if w.isalpha():
            words_no_punkt.append(w.lower())

    my_stopwords = stopwords.words("english")

    for w in words_no_punkt:
        if w not in my_stopwords:
            clean_words.append(w)

    return clean_words

'''
A helper function that creates a frequency distribution of the top ten most common words from a given article
@param topic - the topic selected by the user
@returns - a list of tuples with the top ten words and their corresponding occurrences
'''
def freq_dist(topic):
    words = get_words(topic)
    fdist = FreqDist(words)
    return fdist.most_common(10)

'''
A helper function that creates the line graph figure to display the frequency distribution
@param word_dist - the list of the top ten most common words
@returns - the pyplot line graph figure
'''
def create_figure(word_dist):
    occurrences = []
    words = []
    for c in word_dist:
        words.append(c[0])

    for o in word_dist:
        occurrences.append(o[1])

    fig, ax = plt.subplots(figsize=(10, 10))
    x = words
    y = occurrences
    ax.set_ylabel("Ocurrences")
    ax.set_xlabel("Words")
    ax.plot(x, y)

    return fig

'''
A helper function that creates the wordcloud for the top stories
@param topic - the topic selected by the user
'''
def create_wordcloud_top_stories(topic):
    my_article = pull_api_top_stories(topic)

    abstract_words = ""

    for i in my_article["results"]:
        abstract_words = abstract_words + i["abstract"]

    wordcloud = WordCloud().generate(abstract_words)

    plt.figure(figsize=(12,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("top_articles_wordcloud.png")

'''
A helper function that creates the wordcloud for the most popular articles
@param article_type - the most popular articles based on either views, shares, or emails
@param time_period - the most popular articles from the last day (1), week (7), or month (30)
'''
def create_wordcloud_most_popular(article_type, time_period):
    my_article = pull_api_most_popular(article_type, time_period)

    abstract_words = ""

    for i in my_article["results"]:
        abstract_words = abstract_words + i["abstract"]

    wordcloud = WordCloud().generate(abstract_words)

    plt.figure(figsize=(12,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("most_popular_wordcloud.png")