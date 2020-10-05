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
    '2020-10-04': 'title'
    '1969-06-28': 'Stonewall riots https://en.wikipedia.org/wiki/Stonewall_riots',
    '2013-06-26': 'Repeal of DOMA https://www.americanprogress.org/issues/immigration/news/2013/06/26/68033/what-the-doma-decision-means-for-lgbt-binational-couples/',
    '1969-06-28': 'Stonewall riots https://en.wikipedia.org/wiki/Stonewall_riots',
    '2013-06-26': 'Repeal of DOMA https://www.americanprogress.org/issues/immigration/news/2013/06/26/68033/what-the-doma-decision-means-for-lgbt-binational-couples/',
    '2011-09-20': 'Repeal of DADT https://www.americanprogress.org/issues/lgbtq-rights/reports/2012/09/20/38764/the-repeal-of-dont-ask-dont-tell-1-year-later/',
    '1955-12-20': 'Frank Kameny is fired from his job as an astronomer in the United States Army’s Map Service in Washington, D.C. because of his homosexuality. A few days later he is blacklisted from seeking federal employment.  http://www.thelavendereffect.org/2013/12/20/december-20-in-lgbtq-history-2/',
    '1997-12-17': 'In New Jersey, same-sex couples are given the right to jointly adopt children. reference',
    '1924-12-10': 'The Society for Human Rights was founded https://en.wikipedia.org/wiki/Society_for_Human_Rights',
    '1950-11-11': 'The Mattachine Society was founded https://en.wikipedia.org/wiki/Mattachine_Society',
    '1955-09-21': 'The Daughters of Bilitis becomes the first lesbian rights organization in the United States https://en.wikipedia.org/wiki/Daughters_of_Bilitis',
    '1962-01-01': 'Illinois repeals its sodomy laws, becoming the first U.S. state to decriminalize homosexuality. https://en.wikipedia.org/wiki/LGBT_rights_in_Illinois',
    '1973-12-15': 'The board of the American Psychiatric Association votes to remove homosexuality from its list of mental illnesses. https://www.hrc.org/news/flashbackfriday-today-in-1973-the-apa-removed-homosexuality-from-list-of-me',
    '1974-04-02': 'Kathy Kozachenko becomes the first openly gay American elected to public office https://www.nbcnews.com/feature/nbc-out/meet-lesbian-who-made-political-history-years-harvey-milk-n1174941',
    '1977-11-08': 'Harvey Milk wins a seat on the San Francisco Board of Supervisors https://en.wikipedia.org/wiki/Harvey_Milk',
    '1979-10-14': 'An estimated 75,000 people participate in the National March on Washington for Lesbian and Gay Rights. https://en.wikipedia.org/wiki/National_March_on_Washington_for_Lesbian_and_Gay_Rights',
    '1982-03-02': 'Wisconsin becomes the first U.S. state to outlaw discrimination on the basis of sexual orientation. https://en.wikipedia.org/wiki/LGBT_rights_in_Wisconsin',
    '1988-12-01': 'The World Health Organization organizes the first World AIDS Day to raise awareness of the spreading pandemic. https://www.verywellhealth.com/the-history-of-world-aids-day-48717',
}



# TODO: why did tweet_historicat_event() send a regular get_tweet.py tweet?
# TODO: figure out why history tweet isn't posting


def tweet_historicat_event():
    api = authenticate_api()
    # check events list for date that matches today's date
    years=[]
    today = str(date.today())
    sub = today[6:]
    for v,k in events.items():
    years.append(v)

    matching = [s for s in years if sub in s]
    matchstring = str(matching[0])

    if matchstring in events:  # only tweet if date is today
     today_event =  matchstring + ' : ' +  events[matchstring]
     history_tweet = "This day in LGBTQ history: " + today_event
     print (history_tweet)
     api.update_status(history_tweet)
     print('tweet accomplished')


tweet_historicat_event()
