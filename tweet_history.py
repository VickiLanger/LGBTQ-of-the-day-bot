'''
tweet_history.py: use tweet_historical_events.py to tweet event on day in history
5 October 2020
Linh Nguyen (@BobbyWin16)
'''

from datetime import date
from tweet import authenticate_api
from words_dir.tweet_historical_events import events

import random


# TODO: why did tweet_historicat_event() send a regular get_tweet.py tweet?
# TODO: figure out why history tweet isn't posting


def tweet_historicat_event():
    api = authenticate_api()

    # declare empty string
    history_tweet = ""
    tweet_template = "This day in LGBTQ history: "

    # get today's date
    today = str(date.today())

    # extract month and day
    month_and_day = today[5:]  # slice off the first 5 characters

    # make a list of the events that match month_and_day
    list_of_history_tweets = [key + ": " + val for key, val in events.items() if month_and_day in key]
    length_list_history_tweets = len(list_of_history_tweets)

    '''if list has multiple events for the same month and day,
    then pick random,
    else return the item then update api, if none, no update'''
    # IDEA: generate a thread of tweets if it has multiple events in chronological order

    if length_list_history_tweets != 0:
        if length_list_history_tweets > 1:
            history_tweet = tweet_template + random.choice(list_of_history_tweets)
        else:
            history_tweet = tweet_template + list_of_history_tweets[0]
        api.update_status(history_tweet)
        print('tweet accomplished')
    else:
        print('no tweet today')


tweet_historicat_event()
