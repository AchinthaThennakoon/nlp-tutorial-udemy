import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
from string import punctuation
import re
from sklearn.model_selection import train_test_split

# load tweet data
data_set = []

# Read CSV file and append data to data_set
with open('tweetDataFile.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        tweet_obj = {
            "tweet_id": row[0],
            "text": row[1],
            "label": row[2],
            "topic": row[3]
        }
        data_set.append(tweet_obj)

# Print first few entries to verify (optional)
# print(f"Total tweets loaded: {len(data_set)}")
# print("First tweet:", data_set[0])

# preprocess the text data
class PreprocessTweets:
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    def process_tweets(self, list_of_tweets):
        processed_tweets = []
        for tweet in list_of_tweets:
            if tweet["label"] is not None:
                if tweet["label"] == "positive" or tweet["label"] == "negative":
                    processed_tweets.append((self._process_tweet(tweet["text"]), tweet["label"]))
            else:
                processed_tweets.append((self._process_tweet(tweet["text"]), None))

        return processed_tweets

    def _process_tweet(self, tweet):
        tweet = tweet.lower()  # convert text to lower-case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
        tweet = word_tokenize(tweet)  # remove repeated characters (helloooooooo into hello)

        words = []
        for word in tweet:
            if word not in self._stopwords:
                words.append(word)
        return words

tweet_processor = PreprocessTweets()
# Process the tweets
processed_tweets = tweet_processor.process_tweets(data_set)




def build_vocabulary(preprocessed_training_data):
    # Initialize empty list to store all words
    all_words = []

    # Loop through each preprocessed tweet
    for (words, sentiment) in preprocessed_training_data:
        # Add all words from current tweet to all_words list
        all_words.extend(words)

    # Create frequency distribution of all words
    wordlist = nltk.FreqDist(all_words)
    
    # Get unique words as features
    word_features = wordlist.keys()

    return word_features


# Split processed_tweets into training and testing sets (80% train, 20% test)
preprocessed_training_set, preprocessed_testing_set = train_test_split(
    processed_tweets, test_size=0.2, random_state=42
)

# Build vocabulary from training data
training_data_features = build_vocabulary(preprocessed_training_set)

def extract_features(tweet, word_features):
    """
    Extract features from a tweet based on the provided word features.
    Returns a dictionary where keys are word features and values are booleans indicating presence in the tweet.
    """
    tweet_words = set(tweet)  # Convert tweet to a set for faster lookup
    features = {}
    
    for word in word_features:
        features[word] = (word in tweet_words)
    
    return features


# Extract features for training and testing sets
training_features = nltk.classify.apply_features(extract_features, preprocessed_training_set)
