'''
get_reply.py: choose a reply
26 Feb 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

# TODO: add more replies

REPLIES = (
    'Here\'s our question! \nStick around, we\'ll have another in 3 hours!',
)


def get_reply():
    reply_to_tweet = choice(REPLIES)

    return reply_to_tweet
