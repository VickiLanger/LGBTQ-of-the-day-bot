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
    '2020-10-04': 'title',
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

    '1972-07-01': 'The first Pride march is held in London, attracting around 2000 participants. https://www.bbc.com/news/uk-england-40533612',
    '2005-12-05': 'The Civil Partnership Act passes, granting civil partnership in the UK. https://en.wikipedia.org/wiki/Civil_Partnership_Act_2004',

    '2020-06-15': 'The 1964 Civil Rights Act now also prohibits discrimination based on sexual orientation and gender identity. https://www.nytimes.com/2020/06/15/us/gay-transgender-workers-supreme-court.html',
    '2015-06-26': 'Same-sex marriage is legal throughout the United States. https://www.nytimes.com/2015/06/27/us/supreme-court-same-sex-marriage.html',
    '2009-04-03': 'Same-sex marriage is legal in the state of Iowa. https://en.wikipedia.org/wiki/Same-sex_marriage_in_Iowa',
    '2019-02-16': 'Nyla Rose became the first openly transgender wrestler in history to sign with a major American promotion. https://en.wikipedia.org/wiki/Nyla_Rose',
    '2019-09-25': 'Angelica Ross became the first openly transgender person to host an American presidential forum. https://en.wikipedia.org/wiki/Angelica_Ross',
    '2016-09-16': 'Lilly Singh became the first late-night host to ever publicly identify as bisexual. https://en.wikipedia.org/wiki/A_Little_Late_with_Lilly_Singh',
    '2019-04-02': 'Lori Lightfoot was elected Chicago, Illinois first openly gay mayor. https://www.nbcnews.com/news/us-news/lori-lightfoot-elected-chicago-mayor-will-be-1st-black-woman-n990266'
}



# TODO: why did tweet_historicat_event() send a regular get_tweet.py tweet?
# TODO: figure out why history tweet isn't posting


def tweet_historicat_event():
    api = authenticate_api()
    # check events list for date that matches today's date
    today = str(date.today())
    if today in events:  # only tweet if date is today
     today_event =  today + ' : ' +  events[today]
     history_tweet = "This day in LGBTQ history: " + today_event
     api.update_status(history_tweet)
     print('tweet accomplished')


tweet_historicat_event()
