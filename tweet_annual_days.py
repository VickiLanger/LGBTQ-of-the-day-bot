'''
tweet_annual_days.py: post Remembrance, (inter)national, & Visibility Days to twitter.com
28 October 2020
Vicki Langer (@vicki_langer)
'''

from datetime import date
from tweet import authenticate_api
from words_dir.tweet_annual_events import events

def tweet_annual_event():
    api = authenticate_api()
    
    # declare empty string
    annual_event_tweet = ""
    tweet_template = "Today is "
    
    # get today's date
    today = str(date.today())
    
    # get today's month and day
    month_and_day = today[5:]
    
    # make a list of the events that match month_and_day
    list_of_event_tweets = [key + ": " + val for key, val in events.items() if month_and_day in key]
    length_list_event_tweets = len(list_of_event_tweets)
    
    '''if list has multiple events for the same month and day,
    then pick random,
    else return the item then update api, if none, no update'''
    # IDEA: generate a thread of tweets if it has multiple events

    if length_list_event_tweets != 0:
        if length_list_event_tweets > 1:
            event_tweet = tweet_template + random.choice(list_of_event_tweets)
        else:
            event_tweet = tweet_template + list_of_event_tweets[0]
        api.update_status(event_tweet)
        print('tweet accomplished')
    else:
        print('no tweet today')


tweet_historicat_event()
