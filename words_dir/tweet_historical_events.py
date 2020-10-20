'''
tweet_historical_events.py: list of events used to build "this day in history" tweet
15 September 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more events, their dates, and a reference link

# NOTE: syntax--> 'YYYY-MM-DD': 'title/description & a reference link',
# NOTE: place events in order, oldest to newest
# NOTE: must fit in a tweet, so not longer than this line -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

events = {

    # 1800s
    '1889-11-03': 'Amelio Robles Ávila is born, the first trans man in Mexico who fought in the Mexican Revolution. https://es.wikipedia.org/wiki/Amelio_Robles_%C3%81vila',
    '1895-05-25': 'Oscar Wilde is convicted of "gross indecency" for having a homosexual relationship with Alfred Taylor, and is sentenced to two years hard labour. https://en.wikipedia.org/wiki/Oscar_Wilde#Imprisonment',
    '1898-06-05': 'Federico García Lorca is born in Granada, Spain. He was a really important poet, playwright and prose writer who was shot during the spanish Civil War accused of being homosexual. https://es.wikipedia.org/wiki/Federico_Garc%C3%ADa_Lorca',

    # 1900s
    '1901-06-08': 'Post-Roman times, Marcela and Elisa became the first same-sex marriage in Spain. When it was out they had decieved the priest, they fled the country. Yet, their marriage was never voided. https://en.wikipedia.org/wiki/First_same-sex_marriage_in_Spain',

    # 1910s

    # 1920s
    '1924-12-10': 'The Society for Human Rights was founded. https://en.wikipedia.org/wiki/Society_for_Human_Rights',
    '1926-03-06': 'The Hamilton Lodge Ball of Harlem attracts thousands of cross-dressing men and women https://www.queermusicheritage.com/nov2014hamilton.html',
    '1927-01-19': 'First appearance of "homosexual" in the Congressional Record. https://ucsd.libguides.com/lgbtdocs/timeline',
    '1927-02-08': 'First appearance of "lesbian" in the Congressional Record. https://ucsd.libguides.com/lgbtdocs/timeline',

    # 1930s
    '1932-01-01': '"Man into Woman: An Authentic Record of a Change of Sex," the story of the life of Lili Elbe published. https://en.wikipedia.org/wiki/Lili_Elbe',
    '1935-04-09': 'Sigmund Freud writes "Letter to an American Mother", urging compassion and tolerance for homosexuality. https://commons.wikimedia.org/wiki/File:A_Letter_from_Freud_to_a_mother_of_a_homosexual_-_1935_-_1.jpg',

    # 1940s
    '1945-02-20': 'First appearance of "bisexual" in the Congressional Record. https://ucsd.libguides.com/lgbtdocs/timeline',
    '1947-06-01': 'Lisa Ben publishes "Vice Versa", the earliest known US periodical published especially for lesbians. https://en.wikipedia.org/wiki/Vice_Versa_(magazine)',
    '1948-03-01': 'Alfred Kinsey publishes "Sexual Behavior in the Human Male", concluding that homosexual behavior is not restricted to those who identify as homosexual and that 37% of men have enjoyed homosexual activities at least once. https://www.pbs.org/wgbh/americanexperience/features/stonewall-milestones-american-gay-rights-movement/',

    # 1950s
    '1950-11-11': 'The Mattachine Society was founded https://en.wikipedia.org/wiki/Mattachine_Society',
    '1952-01-12': 'Alan Turing was charged, trialed, and convicted with "gross indeceny" for having a homosexual relationship with his partner, Arnold Murray https://en.wikipedia.org/wiki/Alan_Turing#Conviction_for_indecency',
    '1955-09-21': 'The Daughters of Bilitis becomes the first lesbian rights organization in the United States https://en.wikipedia.org/wiki/Daughters_of_Bilitis',
    '1955-12-20': 'Frank Kameny is fired from his job as an astronomer in the United States Army’s Map Service in Washington DC because of his homosexuality. A few days later he is denied from seeking federal employment. http://www.thelavendereffect.org/2013/12/20/december-20-in-lgbtq-history-2/',

    # 1960s
    '1961-09-11': 'The first US-televised documentary about homosexuality airs on a local station in California. https://en.wikipedia.org/wiki/The_Rejected',
    '1962-01-01': 'Illinois repeals its sodomy laws, becoming the first U.S. state to decriminalize homosexuality. https://en.wikipedia.org/wiki/LGBT_rights_in_Illinois',
    '1966-04-21': 'The Mattachine Society organizes a gay rights “Sip-In.”. http://www.nytimes.com/2016/04/21/nyregion/before-the-stonewall-riots-there-was-the-sip-in.html',
    '1969-06-27': 'Canada decriminalised homosexuality https://en.wikipedia.org/wiki/Criminal_Law_Amendment_Act,_1968%E2%80%9369',
    '1969-06-28': 'Stonewall riots https://en.wikipedia.org/wiki/Stonewall_riots',
    '1969-11-02': 'Craig Rodwell, his partner Fred Sargeant, Ellen Broidy, and Linda Rhodes proposed the first gay pride parade to be held in New York City https://en.wikipedia.org/wiki/Pride_parade#:~:text=On%20November%202%2C%201969%2C%20Craig,ERCHO%20meeting%20in%20Philadelphia.',

    # 1970s
    '1970-06-28': 'Community members in New York City march through the streets to recognize the 1-yr anniversary of the Stonewall riots. This event is now considered the 1st gay pride parade. http://www.pbs.org/wgbh/americanexperience/features/timeline/stonewall/',
    '1972-07-01': 'The first Pride march is held in London, attracting around 2000 participants. https://www.bbc.com/news/uk-england-40533612',
    '1973-01-01': 'Maryland becomes the first state to statutorily ban same-sex marriage. https://www.npr.org/templates/story/story.php?storyId=5164355#:~:text=Maryland%20Judge%20Rejects%20Gay%2DMarriage%20Ban%20A%20Maryland%20circuit%20court,court%20has%20affirmed%20the%20decision.',
    '1973-03-11': 'First meeting of Parents and Friends of Gays https://pflag.org/our-story#:~:text=The%20first%20formal%20meeting%20took,Approximately%2020%20people%20attended.',
    '1973-03-26': 'First meeting of "Parents and Friends of Gays," which goes national as Parents, Families and Friends of Lesbians and Gays (PFLAG) in 1982. https://pflag.org/our-story',
    '1973-12-15': 'The board of the American Psychiatric Association votes to remove homosexuality from its list of mental illnesses. https://www.hrc.org/news/flashbackfriday-today-in-1973-the-apa-removed-homosexuality-from-list-of-me',
    '1974-04-02': 'Kathy Kozachenko becomes the first openly gay American elected to public office https://www.nbcnews.com/feature/nbc-out/meet-lesbian-who-made-political-history-years-harvey-milk-n1174941',
    '1974-05-14': 'The Equality Act of 1974 prohibits discrimination "on the basis of sex, marital status, and sexual orientation, and for other purposes." https://ucsd.libguides.com/lgbtdocs/timeline',
    '1975-01-14': 'First federal gay rights bill is introduced to address discrimination based on sexual orientation (Civil Rights Amendments of 1975). https://www.congress.gov/bill/94th-congress/house-bill/166/all-info',
    '1977-06-28': 'The Front d\'Alliberament Gai de Catalunya calls the first LGBT Pride demonstration in Barcelona when homosexuality was still illegal in Spain. 5000 people participate. https://es.wikipedia.org/wiki/Diversidad_sexual_en_Espa%C3%B1a#El_siglo_XIX_y_principios_del_XX',
    '1977-11-08': 'Harvey Milk wins a seat on the San Francisco Board of Supervisors https://en.wikipedia.org/wiki/Harvey_Milk',
    '1977-07-08': 'João W. Nery became the first brazilian transgender to have undergone sex-change surgery in Brazil https://en.wikipedia.org/wiki/Jo%C3%A3o_W._Nery',
    '1978-01-09': 'Harvey Milk is inaugurated as San Francisco city supervisor, and is the first openly gay man to be elected to a political office in California. http://milkfoundation.org/about/harvey-milk-biography/',
    '1978-06-25': 'The rainbow flag becomes a universal symbol of hope for LGBTQ people around the world https://www.cnn.com/style/article/pride-rainbow-flag-design-history/index.html#:~:text=The%20rainbow%20flag%2C%20which%20has,openly%20gay%20artist%20and%20activist.',
    '1979-10-14': 'An estimated 75,000 people participate in the National March on Washington for Lesbian and Gay Rights. https://en.wikipedia.org/wiki/National_March_on_Washington_for_Lesbian_and_Gay_Rights',
    '1979-01-11': 'The law that decriminalizes homosexuality in Spain comes into force. https://es.wikipedia.org/wiki/Diversidad_sexual_en_Espa%C3%B1a#El_siglo_XIX_y_principios_del_XX',

    # 1980s
    '1982-03-02': 'Wisconsin becomes the first U.S. state to outlaw discrimination on the basis of sexual orientation. https://en.wikipedia.org/wiki/LGBT_rights_in_Wisconsin',
    '1988-12-01': 'The World Health Organization organizes the first World AIDS Day to raise awareness of the spreading pandemic. https://www.verywellhealth.com/the-history-of-world-aids-day-48717',

    # 1990s
    '1993-11-30': 'President Bill Clinton signs a military policy directive that prohibits openly gay and lesbian Americans from serving in the military, but also prohibits the harassment of closeted homosexuals https://www.cnn.com/2013/02/01/us/bill-clinton-fast-facts/index.html',
    '1996-03-12': "Hawaii's Judge Chang rules that the state does not have a legal right to deprive same-sex couples of the right to marry, making Hawaii the first state to recognize that gay and lesbian couples are entitled to the same privileges as heterosexual married couples. https://web.archive.org/web/19990203044430/http://www.cnn.com/US/9612/03/same.sex.marriage/",
    '1997-04-14': 'Comedian Ellen DeGeneres comes out as a lesbian on the cover of Time magazine http://content.time.com/time/covers/0,16641,19970414,00.html',
    '1997-04-30': "DeGeneres' character, Ellen Morgan, on her self-titled TV series 'Ellen' becomes the first leading character to come out on a prime-time network television show. https://en.wikipedia.org/wiki/Ellen_(TV_series)",
    '1997-12-18': 'In New Jersey, same-sex couples are given the right to jointly adopt children. https://www.washingtonpost.com/archive/politics/1997/12/18/nj-allows-gays-to-adopt-jointly/7b031fcd-1338-4dff-b548-1e54eb196f12/',
    '1998-04-01': 'Martin Luther King Jr.`s widow, Coretta Scott King, asks the civil rights community to help in the effort to extinguish homophobia. https://www.cnn.com/2013/08/23/us/coretta-scott-king-fast-facts/index.html',

    # 2000s
    '2001-04-01': 'The Netherlands became the first country to legalize same-sex marriages. https://en.wikipedia.org/wiki/Same-sex_marriage_in_the_Netherlands',
    '2004-05-17': 'The first legal same-sex marriage in the United States takes place in Massachusetts https://www.npr.org/2019/05/17/723649385/the-1st-legally-married-same-sex-couple-wanted-to-lead-by-example',
    '2005-07-03': 'Same-sex marriage becomes legal in Spain. https://es.wikipedia.org/wiki/Matrimonio_entre_personas_del_mismo_sexo_en_Espa%C3%B1a',
    '2005-07-20': 'The enactment of the Civil Marriage Act allows same-sex couples to be married anywhere in Canada. http://laws-lois.justice.gc.ca/eng/acts/c-31.5/page-1.html',
    '2005-09-06': 'The California legislature becomes the first to pass a bill allowing marriage between same-sex couples. Governor Arnold Schwarzenegger vetoes the bill. https://www.nytimes.com/2005/09/06/national/california-legislature-approves-samesex-marriage-bill.html',
    '2005-12-05': 'The Civil Partnership Act passes, granting civil partnership in the UK. https://en.wikipedia.org/wiki/Civil_Partnership_Act_2004',
    '2006-10-25': 'The New Jersey Supreme Court rules that state lawmakers must provide the rights and benefits of marriage to gay and lesbian couples. https://www.cnn.com/2006/US/10/25/gay.marriage/',
    '2008-05-15': 'The California Supreme Court rules in re: Marriage Cases that limiting marriage to opposite-sex couples is unconstitutional. https://www.aclunc.org/our-work/legal-docket/re-marriage-cases',
    '2008-11-04': 'Voters approve Proposition 8 in California, which makes same-sex marriage illegal. The proposition is later found to be unconstitutional by a federal judge. https://en.wikipedia.org/wiki/2008_California_Proposition_8',
    '2009-04-03': 'Same-sex marriage is legal in the state of Iowa. https://en.wikipedia.org/wiki/Same-sex_marriage_in_Iowa',
    '2009-05-16': 'The first monument dedicated to remembering the persecution of homosexuals during the Franco regime is inaugurated in Durango, Spain. https://es.wikipedia.org/wiki/Diversidad_sexual_en_Espa%C3%B1a#El_siglo_XIX_y_principios_del_XX',

    # 2010s
    '2011-05-05': 'Same-sex stable union is now legal in Brazil https://en.wikipedia.org/wiki/LGBT_rights_in_Brazil',
    '2011-09-20': 'Repeal of DADT https://www.americanprogress.org/issues/lgbtq-rights/reports/2012/09/20/38764/the-repeal-of-dont-ask-dont-tell-1-year-later/',
    '2012-05-09': 'In an ABC interview, Obama becomes the first sitting US president to publicly support the freedom for LGBTQ couples to marry https://www.cnn.com/2012/05/09/politics/obama-same-sex-marriage/',
    '2012-06-15': 'Same-sex marriage is now legal in Denmark https://en.wikipedia.org/wiki/LGBT_rights_in_Denmark#Recognition_of_same-sex_relationships',
    '2012-09-30': 'California bans gay "conversion" therapy for minors https://www.reuters.com/article/us-california-gaytherapy-idUSBRE88T0DR20120930',
    '2012-11-06': 'Tammy Baldwin becomes the first openly gay politician and the first Wisconsin woman to be elected to the US Senate https://www.cnn.com/2012/11/07/politics/wisconsin-tammy-baldwin-senate/',
    '2013-05-16': 'Although same-sex unions have been legalized since 2004 in Brazil, only since 2013 is same-sex marriage legal https://en.wikipedia.org/wiki/Same-sex_marriage_in_Brazil',
    '2013-06-26': 'Repeal of DOMA https://www.americanprogress.org/issues/immigration/news/2013/06/26/68033/what-the-doma-decision-means-for-lgbt-binational-couples/',
    '2013-10-24': 'As a less exclusive alternative to "LGBT," "LGBTQ," and "LGBTQIA+," the acronym "GSRM," which stands for "Gender, Sexual, and Romantic Minorities", has been added to Urban Dictionary. ',
    '2014-02-09': 'Michael Sam becomes the first openly gay football player in the NFL https://www.espn.com/espn/otl/story/_/id/10429030/michael-sam-missouri-tigers-says-gay',
    '2015-06-09': 'Secretary of Defense Ash Carter announces that the Military Equal Opportunity policy has been adjusted to include gay and lesbian military members. https://www.cnn.com/2015/06/09/politics/carter-sexual-orientation-policy/index.html',
    '2015-06-26': 'The Supreme Court finally and officially declared same-sex marriage a Constitutional right nationwide https://www.nytimes.com/2015/06/27/us/supreme-court-same-sex-marriage.html',
    '2015-07-23': 'The military allows transgender Americans to serve openly in the military. https://www.advocate.com/politics/military/2015/07/13/reports-pentagon-poised-lift-transgender-military-ban',
    '2015-07-23': 'The Equality Act is introduced. https://en.wikipedia.org/wiki/Equality_Act_United_States',
    '2015-07-27': 'Boy Scouts of America President Robert Gates announces, "the national executive board ratified a resolution removing the national restriction on openly gay leaders and employees" https://www.cnn.com/2015/07/27/us/boy-scouts-gay-leaders-feat/',
    '2015-11-12': 'Indian MP Shashi Tharoor introduced a bill to decriminalise homosexuality but it was rejected by the Lok Sabha. https://www.deccanherald.com/specials/history-of-the-pride-movement-in-india-742950.html',
    '2016-05-17': 'The Senate confirms Eric Fanning to be secretary of the Army, making him the first openly gay secretary of a US military branch https://www.cnn.com/2016/05/17/politics/eric-fanning-secretary-of-the-army/',
    '2016-06-24': 'Obama announces the designation of the first national monument to lesbian, gay, bisexual and transgender LGBTQ rights. https://obamawhitehouse.archives.gov/blog/2016/06/24/president-obama-designates-stonewall-national-monument',
    '2016-06-30': 'Secretary of Defense Carter announces that the Pentagon is lifting the ban on transgender people serving openly in the US military. https://www.cnn.com/2016/06/30/politics/transgender-ban-lifted-us-military/',
    '2016-08-05': 'A record number of "out" athletes compete in the summer Olympic Games in Rio de Janeiro. The Human Rights Campaign estimates that there are at least 41 openly lesbian, gay and bisexual Olympians -- up from 23 that participated in London 2012. https://edition.cnn.com/2016/08/11/sport/rio-2016-lgbt-olympians/',
    '2016-09-16': 'Lilly Singh became the first late-night host to ever publicly identify as bisexual. https://en.wikipedia.org/wiki/A_Little_Late_with_Lilly_Singh',
    '2016-11-09': 'Kate Brown is sworn in as governor of Oregon, a day after she was officially elected to the office. Brown becomes the highest-ranking LGBTQ person elected to office in the United States. https://www.npr.org/sections/thetwo-way/2016/11/09/501338927/for-first-time-openly-lgbt-governor-elected-oregons-kate-brown',
    '2017-06-27': 'District of Columbia residents can now choose a gender-neutral option of their driver`s license.  https://www.cnn.com/2017/06/27/health/washington-gender-neutral-drivers-license/index.html',
    '2017-11-07': 'Virginia voters elect the state`s first openly transgender candidate to the Virginia House of Delegates. Danica Roem unseats incumbent delegate Bob Marshall, who had been elected 13 times over 26 years. https://www.cnn.com/2017/11/07/politics/danica-roem-virginia-transgender/index.html',
    '2018-02-26': 'The Pentagon confirms that the first transgender person has signed a contract to join the US military. https://www.cnn.com/2018/02/26/politics/first-transgender-recruit-join-us-military/index.html',
    '2018-03-23': 'The Trump administration announces a new policy that bans most transgender people from serving in military. After several court battles, the Supreme Court allows the ban to go into effect in January 2019 https://www.cnn.com/2018/03/23/politics/transgender-white-house/index.html',
    '2018-09-06': 'The Supreme Court of India decriminalised Section 377 making gay sex legal. https://timesofindia.indiatimes.com/topic/same-sex-marriage',
    '2018-11-06': 'Democratic US Representative Jared Polis wins the Colorado governor`s race, becoming the nation`s first openly gay man to be elected governor https://www.cnn.com/2018/11/06/politics/jared-polis-colorado-gay-governor/index.html',
    '2019-02-16': 'Nyla Rose became the first openly transgender wrestler in history to sign with a major American promotion. https://en.wikipedia.org/wiki/Nyla_Rose',
    '2019-04-02': 'Lori Lightfoot was elected Chicago, Illinois first openly gay mayor. https://www.nbcnews.com/news/us-news/lori-lightfoot-elected-chicago-mayor-will-be-1st-black-woman-n990266',
    '2019-05-25': 'Transgender no longer recognised as "disorder" by WHO. https://time.com/5596845/world-health-organization-transgender-identity/',
    '2019-06-13': 'Discrimination on the basis of sexual orientation and gender identity became crime in Brazil https://en.wikipedia.org/wiki/LGBT_rights_in_Brazil',
    '2019-09-22': 'Billy Porter becomes the first openly gay black man to win the Emmy for best lead actor in a drama series. https://www.cnn.com/2019/09/22/entertainment/billy-porter-first-openly-gay-black-actor-emmy/index.html',
    '2019-09-25': 'Angelica Ross became the first openly transgender person to host an American presidential forum. https://en.wikipedia.org/wiki/Angelica_Ross',

    # 2020s
    '2020-02-12': 'New Jersey residents can now change the gender marker on a driver`s license without a note from a doctor. https://www.northjersey.com/story/news/new-jersey/2020/02/12/nj-mvc-allow-gender-designation-changes-without-doctors-note/4738926002/',
    '2020-06-15': 'The Supreme Court rules that federal law protects LGBTQ workers from discrimination. https://www.cnn.com/2020/06/15/politics/supreme-court-lgbtq-employment-case/index.html',
    '2020-09-15': 'India`s most populated state, Uttar Pradesh approves setting up of a transgender welfare board in state. https://indianexpress.com/article/cities/lucknow/up-minister-shastri-approves-setting-up-of-transgender-welfare-board-in-state-6597718/',
}
