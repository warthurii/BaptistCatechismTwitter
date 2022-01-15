import sys
import json

with open('catechism.json', 'r') as cat:
    catechism = json.load(cat)

    for qa in catechism:
        q = qa['question']
        a = qa['answer']
        length = len(q) + len(a)
        print(len(a))