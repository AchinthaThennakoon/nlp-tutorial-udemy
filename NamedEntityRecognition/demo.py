from nltk import word_tokenize
from nltk import pos_tag
import nltk

sample_text = "Microsoft Corporation is an American multinational corporation and technology company headquartered in Redmond, Washington. Its best-known software products are the Windows line of operating systems, the Microsoft 365 suite of productivity applications, the Azure cloud computing platform and the Edge web browser."

tokenized_text = word_tokenize(sample_text)
tagged_text = pos_tag(tokenized_text)

named_entity = nltk.ne_chunk(tagged_text)
named_entity.draw()