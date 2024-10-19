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
# print(len(all_words))
# print(all_words["the"])
# print(all_words.most_common(10))

word_features = []
for common_words in all_words.most_common(3000):
    word_features.append(common_words[0])


# function to mark common word present in a review
def find_features(feature_doc):
    words = set(feature_doc)
    features = {}
    for word in word_features:
        is_feature_in_words = word in words
        features[word] = is_feature_in_words

    return features

# print(find_features(movie_reviews.words('neg/cv004_12641.txt')))

feature_sets = []
for (review_word_list, category) in documents:
    feature = (find_features(review_word_list), category)
    feature_sets.append(feature)


train_set = feature_sets[:1500]
test_set = feature_sets[1500:]

classifier = nltk.NaiveBayesClassifier.train(train_set)
score = nltk.classify.accuracy(classifier, test_set)
print('Accuracy : ', score)

classifier.show_most_informative_features(15)