'''
get_tweets.py: mash together a random tweet
10 September 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

from tweet_nouns import nouns
from tweet_adjectives import adjectives
from tweet_labels import labels


def get_tweet():
    tweet_to_send = "today's queerness is a " + choice(adjectives) + " " + choice(labels) + " " + choice(nouns)

    return tweet_to_send
