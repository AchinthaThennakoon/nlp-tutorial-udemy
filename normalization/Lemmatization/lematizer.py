from nltk.stem import WordNetLemmatizer

lemmatizer= WordNetLemmatizer()

print(lemmatizer.lemmatize("puppies"))
print(lemmatizer.lemmatize("wolves"))
print(lemmatizer.lemmatize("are"))
print(lemmatizer.lemmatize("cars"))
print(lemmatizer.lemmatize("people"))
print(lemmatizer.lemmatize("men"))

print("--------")

print(lemmatizer.lemmatize("better",pos="a"))