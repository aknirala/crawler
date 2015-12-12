import string
from collections import Counter

def remove_punctuations(word):
    return word.translate(None, string.punctuation)

with open("ToVectorize.txt") as f:
    print Counter(map(remove_punctuations, f.readlines()[0].split() ))["significant"]
