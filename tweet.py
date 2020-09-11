'''
tweet.py: post tweets to twitter.com
11 September 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
# import time

from os import environ

from get_tweet import get_tweet
# from get_reply import get_reply


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
    except Exception:
        print(f"An error occurred when attempting to authenticate with the twitter API.")


def main():
    api = authenticate_api()
    #reply_with = get_reply()

    print("finding a tweet...")
    tweet = get_tweet()
    print("chose tweet: " + tweet)
    tweet = api.update_status(tweet)  # variable used later for reply to this tweet
    print('tweet has been tweeted')
    #api.update_status(status=reply_with, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    #print('chose reply:' + reply_with)
    #print('reply has been tweeted')


main()
