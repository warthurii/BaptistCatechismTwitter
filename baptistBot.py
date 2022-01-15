import tweepy
import os
import json
import re

def createTwitterObj():
    API_KEY = str(os.getenv('BAPTIST_API_KEY'))
    API_KEY_SECRET = str(os.getenv('BAPTIST_API_KEY_SECRET'))
    ACCESS_TOKEN = str(os.getenv('BAPTIST_ACCESS_TOKEN'))
    ACCESS_TOKEN_SECRET = str(os.getenv('BAPTIST_ACCESS_TOKEN_SECRET'))

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)

def getCatechismStatusText():
    num = 0
    with open('nums.json') as f1:
        nums = json.load(f1)
        num = nums['catechismNum']

    with open('catechism.json', 'r') as catechism:
        catechism = json.load(catechism)

        q = catechism[num]['question']
        a = catechism[num]['answer']
        number = catechism[num]['number']

        statusText = f'Q{number}: {q}\nA: {a}'

    if(len(statusText) > 280):
        words  = re.split('( )', statusText)
        status = ['']
        i = 0
        length = 276
        for word in words:
            if(len(status[i]) + len(str(word)) < length):
                status[i] += str(word)
            else:
                status.append(f'...{word}')
                i += 1
                length = 273
        statusText = status
    
    with open('nums.json', 'w') as f2:
        nums['catechismNum'] = num + 1
        json.dump(nums, f2, indent=4)

    return statusText        

if __name__=="__main__":
    print(getCatechismStatusText())
