'''
get_reply.py: choose a reply
26 Feb 2020
Vicki Langer (@vicki_langer)
'''

from random import choice
from words_dir.tweet_labels import labels


def get_reply(label):
    label_definition = labels[label]
    if (label_definition == ''):
        return

    reply = f'{label.capitalize()}: label_definition'
    return reply
