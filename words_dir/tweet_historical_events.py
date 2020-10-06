'''
tweet_historical_events.py: list of events used to build "this day in history" tweet
15 September 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more events, their dates, and a reference link

from datetime import date

from tweet import authenticate_api

import random

# list of events with date, title, and a reference link

events = {
    '2020-10-07': 'this is a test tweet to see if `def tweet_historicat_event():` works. If you see this, @vicki_langer is super proud, overjoyed, and thankful for @bobbywin16\'s contribution',

    '1969-06-28': 'Stonewall riots https://en.wikipedia.org/wiki/Stonewall_riots',
    '2013-06-26': 'Repeal of DOMA https://www.americanprogress.org/issues/immigration/news/2013/06/26/68033/what-the-doma-decision-means-for-lgbt-binational-couples/',
    '1969-06-28': 'Stonewall riots https://en.wikipedia.org/wiki/Stonewall_riots',
    '2013-06-26': 'Repeal of DOMA https://www.americanprogress.org/issues/immigration/news/2013/06/26/68033/what-the-doma-decision-means-for-lgbt-binational-couples/',
    '2011-09-20': 'Repeal of DADT https://www.americanprogress.org/issues/lgbtq-rights/reports/2012/09/20/38764/the-repeal-of-dont-ask-dont-tell-1-year-later/',
    '1955-12-20': 'Frank Kameny is fired from his job as an astronomer in the United States Army’s Map Service in Washington, D.C. because of his homosexuality. A few days later he is blacklisted from seeking federal employment.  http://www.thelavendereffect.org/2013/12/20/december-20-in-lgbtq-history-2/',
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
    '1952-01-12': 'Alan Turing was charged, trialed, and convicted with "gross indeceny" for having a homosexual relationship with his partner, Arnold Murray https://en.wikipedia.org/wiki/Alan_Turing#Conviction_for_indecency',
    '1972-07-01': 'The first Pride march is held in London, attracting around 2000 participants. https://www.bbc.com/news/uk-england-40533612',
    '2005-12-05': 'The Civil Partnership Act passes, granting civil partnership in the UK. https://en.wikipedia.org/wiki/Civil_Partnership_Act_2004',
    '2009-04-03': 'Same-sex marriage is legal in the state of Iowa. https://en.wikipedia.org/wiki/Same-sex_marriage_in_Iowa',
    '2019-02-16': 'Nyla Rose became the first openly transgender wrestler in history to sign with a major American promotion. https://en.wikipedia.org/wiki/Nyla_Rose',
    '2019-09-25': 'Angelica Ross became the first openly transgender person to host an American presidential forum. https://en.wikipedia.org/wiki/Angelica_Ross',
    '2016-09-16': 'Lilly Singh became the first late-night host to ever publicly identify as bisexual. https://en.wikipedia.org/wiki/A_Little_Late_with_Lilly_Singh',
    '2019-04-02': 'Lori Lightfoot was elected Chicago, Illinois first openly gay mayor. https://www.nbcnews.com/news/us-news/lori-lightfoot-elected-chicago-mayor-will-be-1st-black-woman-n990266',
    '1997-12-18': 'In New Jersey, same-sex couples are given the right to jointly adopt children. https://www.washingtonpost.com/archive/politics/1997/12/18/nj-allows-gays-to-adopt-jointly/7b031fcd-1338-4dff-b548-1e54eb196f12/',
    '1961-09-11': 'The first US-televised documentary about homosexuality airs on a local station in California. https://en.wikipedia.org/wiki/The_Rejected',
    '1973-01-01': 'Maryland becomes the first state to statutorily ban same-sex marriage. https://www.npr.org/templates/story/story.php?storyId=5164355#:~:text=Maryland%20Judge%20Rejects%20Gay%2DMarriage%20Ban%20A%20Maryland%20circuit%20court,court%20has%20affirmed%20the%20decision.',
    '1973-03-11': 'First meeting of Parents and Friends of Gays https://pflag.org/our-story#:~:text=The%20first%20formal%20meeting%20took,Approximately%2020%20people%20attended.',
    '1975-01-14': 'First federal gay rights bill is introduced to address discrimination based on sexual orientation https://www.congress.gov/bill/94th-congress/house-bill/166/all-info',
    '1978-06-25': 'The rainbow flag becomes a universal symbol of hope for LGBTQ people around the world https://www.cnn.com/style/article/pride-rainbow-flag-design-history/index.html#:~:text=The%20rainbow%20flag%2C%20which%20has,openly%20gay%20artist%20and%20activist.',
    '1993-11-30': 'President Bill Clinton signs a military policy directive that prohibits openly gay and lesbian Americans from serving in the military, but also prohibits the harassment of closeted homosexuals https://www.cnn.com/2013/02/01/us/bill-clinton-fast-facts/index.html',
    '1997-04-14': 'Comedian Ellen DeGeneres comes out as a lesbian on the cover of Time magazine http://content.time.com/time/covers/0,16641,19970414,00.html',
    '1998-04-01': 'Martin Luther King Jr.`s widow, Coretta Scott King, asks the civil rights community to help in the effort to extinguish homophobia. https://www.cnn.com/2013/08/23/us/coretta-scott-king-fast-facts/index.html',
    '2004-05-17': 'The first legal same-sex marriage in the United States takes place in Massachusetts https://www.npr.org/2019/05/17/723649385/the-1st-legally-married-same-sex-couple-wanted-to-lead-by-example',
    '2005-09-06': 'The California legislature becomes the first to pass a bill allowing marriage between same-sex couples. Governor Arnold Schwarzenegger vetoes the bill. https://www.nytimes.com/2005/09/06/national/california-legislature-approves-samesex-marriage-bill.html',
    '2006-10-25': 'The New Jersey Supreme Court rules that state lawmakers must provide the rights and benefits of marriage to gay and lesbian couples. https://www.cnn.com/2006/US/10/25/gay.marriage/',
    '2008-05-15': 'The California Supreme Court rules in re: Marriage Cases that limiting marriage to opposite-sex couples is unconstitutional. https://www.aclunc.org/our-work/legal-docket/re-marriage-cases',
    '2008-11-04': 'Voters approve Proposition 8 in California, which makes same-sex marriage illegal. The proposition is later found to be unconstitutional by a federal judge. https://en.wikipedia.org/wiki/2008_California_Proposition_8',
    '2012-05-09': 'In an ABC interview, Obama becomes the first sitting US president to publicly support the freedom for LGBTQ couples to marry https://www.cnn.com/2012/05/09/politics/obama-same-sex-marriage/',
    '2012-11-06': 'Tammy Baldwin becomes the first openly gay politician and the first Wisconsin woman to be elected to the US Senate https://www.cnn.com/2012/11/07/politics/wisconsin-tammy-baldwin-senate/',
    '2015-06-09': 'Secretary of Defense Ash Carter announces that the Military Equal Opportunity policy has been adjusted to include gay and lesbian military members. https://www.cnn.com/2015/06/09/politics/carter-sexual-orientation-policy/index.html',
    '2015-06-26': 'The Supreme Court finally and officially declared same-sex marriage a Constitutional right nationwide https://www.nytimes.com/2015/06/27/us/supreme-court-same-sex-marriage.html',
    '2015-07-23': 'The Equality Act is introduced. https://en.wikipedia.org/wiki/Equality_Act_United_States',
    '2015-07-27': 'Boy Scouts of America President Robert Gates announces, "the national executive board ratified a resolution removing the national restriction on openly gay leaders and employees" https://www.cnn.com/2015/07/27/us/boy-scouts-gay-leaders-feat/',
    '2016-05-17': 'The Senate confirms Eric Fanning to be secretary of the Army, making him the first openly gay secretary of a US military branch https://www.cnn.com/2016/05/17/politics/eric-fanning-secretary-of-the-army/',
    '2016-06-24': 'Obama announces the designation of the first national monument to lesbian, gay, bisexual and transgender LGBTQ rights. https://obamawhitehouse.archives.gov/blog/2016/06/24/president-obama-designates-stonewall-national-monument',
    '2016-06-30': 'Secretary of Defense Carter announces that the Pentagon is lifting the ban on transgender people serving openly in the US military. https://www.cnn.com/2016/06/30/politics/transgender-ban-lifted-us-military/',
    '2016-08-05': 'A record number of "out" athletes compete in the summer Olympic Games in Rio de Janeiro. The Human Rights Campaign estimates that there are at least 41 openly lesbian, gay and bisexual Olympians -- up from 23 that participated in London 2012. https://edition.cnn.com/2016/08/11/sport/rio-2016-lgbt-olympians/',
    '2016-11-09': 'Kate Brown is sworn in as governor of Oregon, a day after she was officially elected to the office. Brown becomes the highest-ranking LGBTQ person elected to office in the United States. https://www.npr.org/sections/thetwo-way/2016/11/09/501338927/for-first-time-openly-lgbt-governor-elected-oregons-kate-brown',
    '2017-06-27': 'District of Columbia residents can now choose a gender-neutral option of their driver`s license.  https://www.cnn.com/2017/06/27/health/washington-gender-neutral-drivers-license/index.html',
    '2017-11-07': 'Virginia voters elect the state`s first openly transgender candidate to the Virginia House of Delegates. Danica Roem unseats incumbent delegate Bob Marshall, who had been elected thirteen times over 26 years. https://www.cnn.com/2017/11/07/politics/danica-roem-virginia-transgender/index.html',
    '2018-02-26': 'The Pentagon confirms that the first transgender person has signed a contract to join the US military. https://www.cnn.com/2018/02/26/politics/first-transgender-recruit-join-us-military/index.html',
    '1969-11-02': 'Craig Rodwell, his partner Fred Sargeant, Ellen Broidy, and Linda Rhodes proposed the first gay pride parade to be held in New York City https://en.wikipedia.org/wiki/Pride_parade#:~:text=On%20November%202%2C%201969%2C%20Craig,ERCHO%20meeting%20in%20Philadelphia.',
    '2018-03-23': 'The Trump administration announces a new policy that bans most transgender people from serving in military. After several court battles, the Supreme Court allows the ban to go into effect in January 2019 https://www.cnn.com/2018/03/23/politics/transgender-white-house/index.html',
    '2018-11-06': 'Democratic US Representative Jared Polis wins the Colorado governor`s race, becoming the nation`s first openly gay man to be elected governor https://www.cnn.com/2018/11/06/politics/jared-polis-colorado-gay-governor/index.html',
    '2019-09-22': 'Billy Porter becomes the first openly gay black man to win the Emmy for best lead actor in a drama series. https://www.cnn.com/2019/09/22/entertainment/billy-porter-first-openly-gay-black-actor-emmy/index.html',
    '2020-06-15': 'The Supreme Court rules that federal law protects LGBTQ workers from discrimination. https://www.cnn.com/2020/06/15/politics/supreme-court-lgbtq-employment-case/index.html',
}


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
    month_and_day = today[5:]

    # make a list of the events that match month_and_day
    list_of_history_tweets = [key + ": " + val for key, val in events.items() if month_and_day in key]
    length_list_history_tweets = len(list_of_history_tweets)

    '''if list has multiple events for the same month and day,
    then pick random,
    else return the item then update api, if none, no update'''
    # IDEA: generate a thread of tweets if has multiple events in chronological order

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
