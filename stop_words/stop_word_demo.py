from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
# print(stop_words)

sample_text = "i was walking by the road when I saw the cutest puppy on other side of the road"
tokenized_text = word_tokenize(sample_text)

filtered_words = []

for word in tokenized_text:
    if word not in stop_words:
        filtered_words.append(word)

print(filtered_words)
