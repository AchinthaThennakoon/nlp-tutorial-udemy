from nltk import word_tokenize,sent_tokenize
from nltk import pos_tag

sample_text = "i was walking by the road when I saw the cutest puppy on other side of the road"
tokenized_text = word_tokenize(sample_text)
tagged_text = pos_tag(tokenized_text)
print(tagged_text)

