'''
tweet_annual_events.py: list of events to be tweeted on their repective date
28 October 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more events, their dates, and a reference link

# NOTE: syntax--> 'MM-DD': 'Name of day \n relevant hashtag',  # reference link, if you have one
# NOTE: place events in order
# NOTE: must fit in a tweet, so not longer than this line -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# NOTE: For events that are on a nth day of the month (like 2nd Tuesday of November), the syntax is 'MM-xY' where x is the week number and Y is the day of the week
#       denoted by MTWRFSU - Monday, Tuesday, Wednesday, thuRsday, Friday, Saturday, sUnday
#       Example - 2nd Tuesday of November would be listed as '11-2T'

# NOTE: If multiple events fall on the same date, convert that entry to a list
#       e.g. 'mm-dd': [events]
#       Or, if an event already exists in this list, convert it
#       from 'mm-dd': 'old event'
#       to 'mm-dd': ['old event',
#                   'new event 1',
#                   'new event 2',

events = {
    # January
    '01-29': 'Brazilian National Transgender Day of Visibility 🏳️‍️⚧️', #https://justica.sp.gov.br/index.php/coordenacoes-e-programas/coordenacao-de-politicas-para-a-diversidade-sexual/calendario-de-datas-afirmativas/

    # February

    # March
    '03-01': 'Zero Discrimination Day 🖤🤎🏳️‍️⚧️❤🧡💛💚💙💜',  # https://www.unaids.org/en/zero-discrimination-day
    '03-31': 'International Transgender Day of Visibility 🏳️‍️⚧️\n#TransDayOfVisibility #TDOV',  # http://www.transstudent.org/tdov

    # April
    '04-06': 'International Asexuality Day 🖤💜🤍 \n#InternationalAceDay',  # https://internationalasexualityday.org/en/
    '04-26': 'Lesbian Visibility Day 🤎🧡🤍💖',  # https://www.queerevents.ca/notable-lgbtq-dates#lesbianvisibilityday

    # May
    '05-08': 'The birthday of Tom of Finland (1920–91), often called Finland\'s most famous artist globally. \n #TomOfFinlandDay' # https://finland.fi/arts-culture/tom-of-finland-and-idahotb-both-continue-to-contribute-to-pride-and-acceptance/
    '05-17': 'International Day Against Homophobia, Transphobia, and Biphobia 🖤🤎🏳️‍️⚧️❤🧡💛💚💙💜',  # https://may17.org/
    '05-19': 'Agender Pride Day  🖤🤍💚🤍🖤',  # https://www.northshorepride.org/event/agender-pride-day/
    '05-22': 'Harvey Milk Day \n#HarveyMilkDay #HMD',  # https://www.northshorepride.org/event/harvey-milk-day/
    '05-24': 'Pansexual and Panromantic Awareness and Visibility Day 💖💛💙',  # https://lgbt.foundation/news/5-things-you-should-know-on-pansexual-visibility-day/161

    # June
    '06-12': 'Pulse Night of Remembrance',  # https://www.northshorepride.org/event/pulse-night-of-remembrance/
    '06-23': 'Alan Mathison Turing was an English mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist. \n #AlanTuringDay', # https://en.wikipedia.org/wiki/Alan_Turing


    # July
    '07-14': 'International Non-Binary People\'s Day 💛🤍💜🖤',  # https://en.wikipedia.org/wiki/International_Non-Binary_People%27s_Day

    # August
    '08-2U': 'Gay Uncles Day',  # https://www.today.com/parents/gay-uncles-day-2020-how-being-guncle-changed-my-perception-t188917
    '08-29': 'Brazilian National Lesbian Day of Visibility', #https://justica.sp.gov.br/index.php/coordenacoes-e-programas/coordenacao-de-politicas-para-a-diversidade-sexual/calendario-de-datas-afirmativas/

    # September
    '09-16': 'Bisexual+ Awareness Week 💖💜💙',  # https://en.wikipedia.org/wiki/Celebrate_Bisexuality_Day
    '09-17': 'Bisexual+ Awareness Week 💖💜💙',  # https://en.wikipedia.org/wiki/Celebrate_Bisexuality_Day
    '09-18': 'Bisexual+ Awareness Week 💖💜💙',  # https://en.wikipedia.org/wiki/Celebrate_Bisexuality_Day
    '09-19': 'Bisexual+ Awareness Week 💖💜💙',  # https://en.wikipedia.org/wiki/Celebrate_Bisexuality_Day
    '09-20': 'Bisexual+ Awareness Week 💖💜💙',  # https://en.wikipedia.org/wiki/Celebrate_Bisexuality_Day
    '09-21': 'Bisexual+ Awareness Week 💖💜💙',  # https://en.wikipedia.org/wiki/Celebrate_Bisexuality_Day
    '09-22': 'Bisexual+ Awareness Week 💖💜💙',  # https://en.wikipedia.org/wiki/Celebrate_Bisexuality_Day
    '09-23': 'Celebrate Bisexuality Day 💖💜💙',  # https://en.wikipedia.org/wiki/Celebrate_Bisexuality_Day

    # October
    '10-08': 'International Lesbian Day 🤎🧡🤍💖',  # https://en.wikipedia.org/wiki/List_of_LGBT_awareness_periods
    '10-11': 'National Coming Out Day 🚪',  # http://www.hrc.org/resources/the-history-of-coming-out
    '10-16': 'Oscar Fingal O\'Flahertie Wills Wilde was an Irish poet and playwright. \n #OscarWildeDay', # https://en.wikipedia.org/wiki/Oscar_Wilde
    '10-20': 'Intersex Awareness Day 💛💜',  # http://intersexday.org/en/intersex-awareness-day/
    '10-22': 'Asexual Awareness Week 🖤💜🤍',  # http://www.asexualawarenessweek.com/index.html
    '10-23': 'Asexual Awareness Week 🖤💜🤍',  # http://www.asexualawarenessweek.com/index.html
    '10-24': 'Asexual Awareness Week 🖤💜🤍',  # http://www.asexualawarenessweek.com/index.html
    '10-25': 'Asexual Awareness Week 🖤💜🤍',  # http://www.asexualawarenessweek.com/index.html
    '10-26': 'Asexual Awareness Week 🖤💜🤍',  # http://www.asexualawarenessweek.com/index.html
    '10-27': 'Asexual Awareness Week 🖤💜🤍',  # http://www.asexualawarenessweek.com/index.html
    '10-28': 'Asexual Awareness Week 🖤💜🤍',  # http://www.asexualawarenessweek.com/index.html
    '10-29': 'the day for not so regularly scheduled testing in production. \n \nIf you see this, it was a success and we will soon see tweets for remembrance, (inter)national, & Visibility Days/weeks',
    '10-5F': 'a good day for testing yet another feature in production. We now support annual events with variable dates like "5th Friday of October"',

    # November
    '11-1U': 'Trans Parent Day',  # http://transparentday.org/
    '11-08': 'Intersex Solidarity Day 💛💜 \n #IntersexSolidarityDay',
    '11-13': 'Transgender Awareness Week 🏳️‍️⚧️\n #TransAwarenessWeek',  # https://www.glaad.org/transweek
    '11-14': 'Transgender Awareness Week 🏳️‍️⚧️\n #TransAwarenessWeek',  # https://www.glaad.org/transweek
    '11-15': 'Transgender Awareness Week 🏳️‍️⚧️\n #TransAwarenessWeek',  # https://www.glaad.org/transweek
    '11-16': 'Transgender Awareness Week 🏳️‍️⚧️\n #TransAwarenessWeek',  # https://www.glaad.org/transweek
    '11-17': 'Transgender Awareness Week 🏳️‍️⚧️\n #TransAwarenessWeek',  # https://www.glaad.org/transweek
    '11-18': 'Transgender Awareness Week 🏳️‍️⚧️\n #TransAwarenessWeek',  # https://www.glaad.org/transweek
    '11-19': 'Transgender Awareness Week 🏳️‍️⚧️\n #TransAwarenessWeek',  # https://www.glaad.org/transweek
    '11-20': 'International Transgender Day of Remembrance 🏳️‍️⚧️\n #TransDayOfRemembrance',  # http://tdor.info/about-2/

    # December
    '12-01': 'World AIDS day \n #WorldAIDSDay',  # http://www.worldaidsday.org/about
    '12-08': 'Pansexual Pride Day 💖💛💙',  # https://www.queerevents.ca/notable-lgbtq-dates#pansexualprideday
    '12-10': 'Human Rights Day \n #HumanRightsDay',  # https://www.un.org/en/observances/human-rights-day
}
