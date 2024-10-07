from nltk.tokenize import sent_tokenize, word_tokenize

sample_text = "hello there Mr. Brown, how are you? The weather is nice. how is your mother in law doing"

tokenized_sentences = sent_tokenize(sample_text)
for sentence in tokenized_sentences:
    print(sentence)

tokenized_words = word_tokenize(sample_text)
for word in tokenized_words:
    print(word)