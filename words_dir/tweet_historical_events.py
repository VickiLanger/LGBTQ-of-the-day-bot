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

    '1966-04-21': 'The Mattachine Society organizes a gay rights “Sip-In.”. http://www.nytimes.com/2016/04/21/nyregion/before-the-stonewall-riots-there-was-the-sip-in.html',
    '2015-07-23': 'The Equality Act is introduced. http://www.hrc.org/resources/the-equality-act',

    '1961-09-11': 'The first US-televised documentary about homosexuality airs on a local station in California. https://diva.sfsu.edu/collections/sfbatv/bundles/225539',
    '1970-06-28': 'Community members in New York City march through the local streets to recognize the one-year anniversary of the Stonewall riots. This event is named Christopher Street Liberation Day and is now considered the first gay pride parade. http://www.pbs.org/wgbh/americanexperience/features/timeline/stonewall/',
    '1973-03-26': 'First meeting of "Parents and Friends of Gays," which goes national as Parents, Families and Friends of Lesbians and Gays (PFLAG) in 1982. https://pflag.org/our-story',
    '1978-01-09': 'Harvey Milk is inaugurated as San Francisco city supervisor, and is the first openly gay man to be elected to a political office in California. http://milkfoundation.org/about/harvey-milk-biography/',
    '1996-03-12': "Hawaii's Judge Chang rules that the state does not have a legal right to deprive same-sex couples of the right to marry, making Hawaii the first state to recognize that gay and lesbian couples are entitled to the same privileges as heterosexual married couples. https://web.archive.org/web/19990203044430/http://www.cnn.com/US/9612/03/same.sex.marriage/",
    '1997-04-30': "DeGeneres' character, Ellen Morgan, on her self-titled TV series 'Ellen' becomes the first leading character to come out on a prime-time network television show. https://en.wikipedia.org/wiki/Ellen_(TV_series)",
    '2004-05-17': 'The first legal same-sex marriage in the United States takes place in Massachusetts. https://www.npr.org/2019/05/17/723649385/the-1st-legally-married-same-sex-couple-wanted-to-lead-by-example',
    '2006-10-25': 'The New Jersey Supreme Court rules that state lawmakers must provide the rights and benefits of marriage to gay and lesbian couples. http://www.cnn.com/2006/US/10/25/gay.marriage/',
    '2012-05-09': 'In an ABC interview, Obama becomes the first sitting US president to publicly support the freedom for LGBTQ couples to marry. http://www.cnn.com/2012/05/09/politics/obama-same-sex-marriage/',
    '2012-11-06': 'Tammy Baldwin becomes the first openly gay politician and the first Wisconsin woman to be elected to the US Senate. http://www.cnn.com/2012/11/07/politics/wisconsin-tammy-baldwin-senate/',
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
