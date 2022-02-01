import tweepy
import os
import json
import re


def createTwitterObj():
    API_KEY = str(os.getenv("BAPTIST_API_KEY"))
    API_KEY_SECRET = str(os.getenv("BAPTIST_API_KEY_SECRET"))
    ACCESS_TOKEN = str(os.getenv("BAPTIST_ACCESS_TOKEN"))
    ACCESS_TOKEN_SECRET = str(os.getenv("BAPTIST_ACCESS_TOKEN_SECRET"))
    BEARER_TOKEN = str(os.getenv("BAPTIST_BEARER_TOKEN"))

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # return tweepy.Client(
    #     bearer_token=BEARER_TOKEN,
    #     consumer_key=API_KEY,
    #     consumer_secret=API_KEY_SECRET,
    #     access_token=ACCESS_TOKEN,
    #     access_token_secret=ACCESS_TOKEN_SECRET,
    # )

    return tweepy.API(auth)


def getCatechismStatusText():
    num = 0
    with open("nums.json") as f1:
        nums = json.load(f1)
        num = nums["catechismNum"]

    if num >= 114:
        return ""

    with open("catechism.json", "r") as catechism:
        catechism = json.load(catechism)

        q = catechism[num]["question"]
        a = catechism[num]["answer"]
        number = catechism[num]["number"]

        statusText = [f"Q{number}: {q}\nA: {a}"]

    if len(statusText[0]) > 280:
        words = re.split("( )", statusText[0])
        status = [""]
        i = 0
        length = 276
        for word in words:
            if len(status[i]) + len(str(word)) < length:
                status[i] += str(word)
            else:
                status.append(f"... {word}")
                i += 1
                length = 273
        statusText = status

    with open("nums.json", "w") as f2:
        nums["catechismNum"] = num + 1
        json.dump(nums, f2, indent=4)

    return statusText


def tweetQA():
    status = getCatechismStatusText()

    if status == "":
        return

    tweeter = createTwitterObj()

    tweet = False
    for part in status:
        print(part)
        print(len(part))
        tweet = tweeter.update_status(
            status=part, in_reply_to_status_id=tweet.id if tweet else None
        )


if __name__ == "__main__":
    tweetQA()
