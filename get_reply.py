'''
get_reply.py: choose a reply
26 Feb 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

# TODO: add more replies

REPLIES = { 
    'gay': 'definition goes here',
    '': '',
    '': '',
    '': '',
    '': '',
}


def get_reply():
    #if label == 
    reply_to_tweet = choice(REPLIES)

    return reply_to_tweet
