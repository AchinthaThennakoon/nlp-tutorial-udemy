from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

with open('description.txt','r') as corpora:
    sample_text = corpora.read()

tokenized_sent = sent_tokenize(sample_text)
filtered_words = []

for sent in tokenized_sent:
    tokenized_text = word_tokenize(sent)

    for word in tokenized_text:
        if word not in stop_words:
            filtered_words.append(word)

print(filtered_words)