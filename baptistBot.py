import tweepy
import os

def createTwitterObj():
    API_KEY = str(os.getenv('BAPTIST_API_KEY'))
    API_KEY_SECRET = str(os.getenv('BAPTIST_API_KEY_SECRET'))
    ACCESS_TOKEN = str(os.getenv('BAPTIST_ACCESS_TOKEN'))
    ACCESS_TOKEN_SECRET = str(os.getenv('BAPTIST_ACCESS_TOKEN_SECRET'))

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)

if __name__=="__main__":
    tweeter = createTwitterObj()
    tweeter.update_status('Hello\nWorld')