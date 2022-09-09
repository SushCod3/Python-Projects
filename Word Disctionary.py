import json

with open('dictionary.json') as dict:
    data = json.load(dict)

while True:
    word = input('\nEnter your word: ')
    print(data[word])