import os
import json
import hashlib
import datetime
import tweepy

def get_tweet():
    with open('tweets.json', 'r', encoding='utf-8') as f:
        tweets = json.load(f)
    
    now = datetime.datetime.utcnow()
    seed = f"{now.year}-{now.month}-{now.day}-{now.hour}"
    index = int(hashlib.md5(seed.encode()).hexdigest(), 16) % len(tweets)
    return tweets[index]

def post_tweet():
    client = tweepy.Client(
        consumer_key=os.environ['API_KEY'],
        consumer_secret=os.environ['API_SECRET'],
        access_token=os.environ['ACCESS_TOKEN'],
        access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
    )
    
    tweet_text = get_tweet()
    response = client.create_tweet(text=tweet_text)
    print(f"Tweet atıldı: {tweet_text[:80]}...")

if __name__ == '__main__':
    post_tweet()
