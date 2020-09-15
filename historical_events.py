'''
historical_events.py: list of events used to build "this day in history" tweet
15 September 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more events, their dates, and a reference link

import datetime

from tweet import authenticate_api


# list of events with date, title, and a reference link
events = [
    ('1969-06-28', 'Stonewall riots', 'https://en.wikipedia.org/wiki/Stonewall_riots'),
    ('2013-06-26', 'Repeal of DOMA', 'https://www.americanprogress.org/issues/immigration/news/2013/06/26/68033/what-the-doma-decision-means-for-lgbt-binational-couples/'),
    ('2011-09-20', 'Repeal of DADT', 'https://www.americanprogress.org/issues/lgbtq-rights/reports/2012/09/20/38764/the-repeal-of-dont-ask-dont-tell-1-year-later/'),
    ('1955-12-20', 'Frank Kameny is fired from his job as an astronomer in the United States Army’s Map Service in Washington, D.C. because of his homosexuality. A few days later he is blacklisted from seeking federal employment. ', 'http://www.thelavendereffect.org/2013/12/20/december-20-in-lgbtq-history-2/'),
    # ('1997-12-17', 'In New Jersey, same-sex couples are given the right to jointly adopt children.', 'reference'),
    ('2019-09-15', 'this is a test of the "this day in queer history" tweets', 'https://twitter.com/vicki_langer/status/1305686553927315459?s=20'),
    ('date', 'title', 'reference'),
    ('date', 'title', 'reference'),
]

# TODO: why did tweet_historicat_event() send a regular get_tweet.py tweet?
# TODO: line 20, TypeError: 'tuple' object is not callable

def tweet_historicat_event():
    api = authenticate_api()
    # check events list for date that matches today's date
    count = 0
    for event in events:
        date = events[count][0]  # get date from 1st element in tuple from list
        today = datetime.now()
        count = count + 1  # save the current iteration in a variable
        if date == today:  # only tweet if date is today
            title = events[count][1]  # get date from 2nd element in tuple from list
            reference_link = events[count][2]  # get date from 3rd element in tuple from list
            history_tweet = f"This day in LGBTQ history: {title}\n\n{reference_link}"
            history_tweet = api.update_status(history_tweet)
            print('tweet accomplished')


tweet_historicat_event()
