'''
tweet_historical_events.py: list of events used to build "this day in history" tweet
15 September 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more events, their dates, and a reference link

from datetime import date

from tweet import authenticate_api


# list of events with date, title, and a reference link
events = {
'1969-06-28': 'Stonewall riots https://en.wikipedia.org/wiki/Stonewall_riots',
'2013-06-26': 'Repeal of DOMA https://www.americanprogress.org/issues/immigration/news/2013/06/26/68033/what-the-doma-decision-means-for-lgbt-binational-couples/',
'2020-10-04': 'title'}


# TODO: why did tweet_historicat_event() send a regular get_tweet.py tweet?
# TODO: figure out why history tweet isn't posting


def tweet_historicat_event():
    api = authenticate_api()
    # check events list for date that matches today's date
    today = str(date.today())
    if today in events:  # only tweet if date is today
     today_event =  today + ' : ' +  events[today]
     history_tweet = "This day in LGBTQ history: " today_event
     api.update_status(history_tweet)
     print('tweet accomplished')


tweet_historicat_event()
