import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
# nltk.download('punkt')
stemmer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag



# a = "how was your day?"
# print(a)
# print(tokenize(a))

# words = ["rational", "rationalize"]
# stemmed_words = [stem(word) for word in words]
# print(stemmed_words)

sent = ["hi", "how", "are", "you", "doin"]
all_words = ["hi", "there", "is", "you", "wondering", "in", "cold"]
r = bag_of_words(sent,all_words)
# print(r)