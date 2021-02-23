'''
tweet_annual_days.py: post Remembrance, (inter)national, & Visibility Days to twitter.com
28 October 2020
Vicki Langer (@vicki_langer)
'''

from datetime import date
from math import ceil
from tweet import authenticate_api
from words_dir.tweet_annual_events import events
from random import choice


def tweet_annual_event():
    api = authenticate_api()

    events_today = []

    def add_events(events_to_add):
        # extend events list if a list of multiple events are given
        if isinstance(events_to_add, list):
            events_today.extend(events_to_add)
        else:
            events_today.append(events_to_add)

    # get today's date
    date_today = date.today()
    today = str(date_today)

    month = today[5:7]
    day = today[8:10]

    # GET EVENTS TODAY

    # get today's month and day
    month_and_day = f'{month}-{day}'

    # find and add events matching the case
    add_events(events.get(month_and_day, []))

    # GET RELATIVE EVENTS THAT RESOLVE TO TODAY

    # get today's weekday - 0-6 = Monday-Sunday
    weekday_index = date_today.weekday()

    # convert to letter
    # MTWRFSU - Monday, Tuesday, Wednesday, thuRsday, Friday, Saturday, sUnday

    weekday_letters = "MTWRFSU"
    weekday = weekday_letters[weekday_index]

    # determine which week we are in
    week = ceil(int(day) / 7)
    # create the code to look up - format 'MM-nU' would be the nth sUnday of the current Month
    nth_weekday_of_month = f'{month}-{week}{weekday}'

    # find and add events matching the case
    add_events(events.get(nth_weekday_of_month, []))

    '''Pick a random Event from the list of events today and tweet it'''
    # IDEA: generate a thread of tweets if it has multiple events

    if events_today:
        chosen_event = choice(events_today)
        event_tweet = f'Today is {chosen_event}'
        api.update_status(event_tweet)
        print('annual event tweet accomplished')
    else:
        print('no annual event tweet today')


tweet_annual_event()
