'''
get_tweets.py: grab a random tweet
10 September 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

from tweets import TWEETS


def get_tweet():
    tweet_to_send = choice(TWEETS)

    return tweet_to_send
