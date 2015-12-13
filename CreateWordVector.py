import string
import json
from collections import Counter



def remove_punctuations(word):
    return word.translate(None, string.punctuation)

with open("20151116.json") as json_file:
    json_data = json.load(json_file)
    s = ''
    for d in json_data:
        s += d['content']
    print(Counter(  s.split()  ))
    # Why is the below line giving error?
    # print(Counter( map(remove_punctuations,  s.split())  ))
    # pprint(Counter(map(remove_punctuations, json_file.readlines()[0].split() )))
