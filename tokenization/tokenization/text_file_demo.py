from nltk.tokenize import sent_tokenize,word_tokenize

file_path = "sample.txt"
text = open(file_path,"r").read()

print(text)
print("---------------")


tokenized_sentences = sent_tokenize(text)
for sentence in tokenized_sentences:
    print(sentence)


print("---------------")

tokenized_words = word_tokenize(text)
for word in tokenized_words:
    print(word)