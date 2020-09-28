'''
Luis F. Hernandez JR
5163353
'''

import json
import requests

from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def save_to_file(data, filename):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file, indent = 2)

def read_from_file(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
    return data

def pull_api(topic):
    api_key_dict = read_from_file("JSON_Files/api_key.json")
    api_key = api_key_dict["my_key"]

    url = "https://api.nytimes.com/svc/topstories/v2/" + topic + ".json?api-key=" + api_key

    response = requests.get(url).json()

    save_to_file(response, "JSON_Files/response.json")

    return read_from_file("JSON_Files/response.json")

def get_words(topic):
    my_article = pull_api(topic)

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

def freq_dist(topic):
    words = get_words(topic)
    fdist = FreqDist(words)
    return fdist.most_common(10)

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

def create_wordcloud(topic):
    my_article = pull_api(topic)

    abstract_words = ""

    for i in my_article["results"]:
        abstract_words = abstract_words + i["abstract"]

    wordcloud = WordCloud().generate(abstract_words)

    plt.figure(figsize=(12,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("Images/wordcloud.png")