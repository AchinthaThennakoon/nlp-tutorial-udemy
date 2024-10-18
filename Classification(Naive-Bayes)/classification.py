import nltk
from nltk.corpus import movie_reviews
import random

documents = []

# print(movie_reviews.categories())
#
# # Displays frequency of words in ‘movie_reviews’
# print(nltk.FreqDist(movie_reviews.words()))

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        review_word_list = list(movie_reviews.words(fileids=fileid))
        document = (review_word_list, category)
        documents.append(document)

# print(documents[0])

random.shuffle(documents)

all_words = []
for word  in movie_reviews.words():
    all_words.append(word.lower())

all_words = nltk.FreqDist(all_words)
print(len(all_words))
print(all_words["the"])