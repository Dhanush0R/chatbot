import nltk
from nltk.stem.porter import PorterStemmer
# nltk.download('punkt')
stemmer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words():
    pass

# a = "how was your day?"
# print(a)
# print(tokenize(a))

words = ["rational", "rationalize"]
stemmed_words = [stem(word) for word in words]
print(stemmed_words)