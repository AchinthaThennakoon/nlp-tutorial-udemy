from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

# sample_words = ["legal","illegal","legally","legalize","Legal"]
# for word in sample_words:
#     print(stemmer.stem(word))
#

plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
         'died', 'agreed', 'owned', 'humbled', 'sized',
        'meeting', 'stating', 'siezing', 'itemization',
         'sensational', 'traditional', 'reference', 'colonizer',
        'plotted']

singles = [stemmer.stem(plural) for plural in plurals]

print(' '.join(singles))