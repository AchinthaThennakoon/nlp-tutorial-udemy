import nltk
from nltk.corpus import movie_reviews
import random

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        review_word_list = list(movie_reviews.words(fileids=fileid))
        document = (review_word_list, category)
        documents.append(document)


random.shuffle(documents)

all_words = []
for word  in movie_reviews.words():
    all_words.append(word.lower())

all_words = nltk.FreqDist(all_words)
print(len(all_words))
print(all_words["the"])