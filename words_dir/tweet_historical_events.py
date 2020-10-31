'''
tweet_historical_events.py: list of events used to build "this day in history" tweet
15 September 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more events, their dates, and a reference link

# NOTE: syntax--> 'YYYY-MM-DD': 'title/description & a reference link',
# NOTE: place events in order, oldest to newest
# NOTE: must fit in a tweet, so not longer than this line or max of 287 characters ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

events = {
    # 1600s
    '1610-05-24': 'The Virginia Colony formally outlawed "Sodomie." http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1610s/sodomy-law-virginia-may-24-161',
    '1629-01-01': 'In 1629, the General Court of Colonial Virginia met to decide if a certain settler was male or female. https://www.history.com/news/intersex-people-casimir-pulaski-thomasine-hall',
    '1636-11-13': 'The Plymouth, America colony listed sodomy as one of 8 offenses punishable by death. http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1630s/sodomy-law-plymouth-november-1',
    '1637-08-06': 'John Alexander and Thomas Roberts were found guilty by the Plymouth court for "lewd behavior and unclean carriage one with another." http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1630s/legal-case-allexander-roberts-',
    '1642-03-01': 'Edward Michell and Edward Preston were cited by the Plymouth court for "lewd & sodomitical practices" with one another. They were both whipped as punishment. http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1640s/legal-case-michell-and-preston', 
    '1642-12-01': 'The General Court of Connecticut listed "man lying with man" as one of 12 capital crimes, along with witchcraft and blasphemy. http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1640s/sodomy-law-connecticut-decembe',
    '1642-12-05': 'Elizabeth Johnson was sentenced to be whipped and fined for "unseemly practices betwixt her and another maid" as well as being stubborn and plugging her ears. http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1640s/legal-case-elizabeth-johnson-m',
    '1646-03-25': 'Jan Creoli, a black man in the New Netherland Colony (now New York) was brutally and publicly executed after being accused of sodomy. http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1640s/sodomy-case-creoli-executed-ne',
    '1649-03-06': 'Sara Norman and Mary Hammon were publicly shamed for participating in "unchaste behavior" together. http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1640s/legal-case-norman-and-hammon-p',

    # 1700s
    '1700-11-27': 'Pennsylvania replaced it\'s previous sodomy statute with two separate laws. Whites were sentenced to life imprisonment, while blacks were sentenced to death. http://outhistory.org/exhibits/show/the-age-of-sodomitical-sin/1700s/sodomy-law-pennsylvania-noveme',

    # 1800s
    '1871-01-01': 'Homosexuality was technically made illegal in Germany in 1871, but it was rarely enforced until the Nazi Party took power in 1933. https://www.history.com/news/pink-triangle-nazi-concentration-camps',
    '1889-11-03': 'Amelio Robles Ávila is born, the first trans man in Mexico who fought in the Mexican Revolution. https://es.wikipedia.org/wiki/Amelio_Robles_%C3%81vila',
    '1895-05-25': 'Oscar Wilde is convicted of "gross indecency" for having a homosexual relationship with Alfred Taylor and is sentenced to two years hard labour. https://en.wikipedia.org/wiki/Oscar_Wilde#Imprisonment',
    '1898-06-05': 'Federico García Lorca is born in Granada, Spain. He was a really important poet, playwright, and prose writer who was shot during the Spanish Civil War, accused of being homosexual. https://es.wikipedia.org/wiki/Federico_Garc%C3%ADa_Lorca',

    # 1900s
    '1901-06-08': 'Post-Roman times, Marcela and Elisa became the first same-sex marriage in Spain. When it was out that they had deceived the priest, they fled the country. Yet, their marriage was never voided. https://en.wikipedia.org/wiki/First_same-sex_marriage_in_Spain',

    # 1910s

    # 1920s
    '1924-12-10': 'The Society for Human Rights was founded. https://en.wikipedia.org/wiki/Society_for_Human_Rights',
    '1926-03-06': 'The Hamilton Lodge Ball of Harlem attracts thousands of cross-dressing men and women. https://www.queermusicheritage.com/nov2014hamilton.html',
    '1927-01-19': 'First appearance of "homosexual" in the Congressional Record. https://ucsd.libguides.com/lgbtdocs/timeline',
    '1927-02-08': 'First appearance of "lesbian" in the Congressional Record. https://ucsd.libguides.com/lgbtdocs/timeline',

    # 1930s
    '1932-01-01': '"Man into Woman: An Authentic Record of a Change of Sex," the story of the life of Lili Elbe published. https://en.wikipedia.org/wiki/Lili_Elbe',
    '1935-04-09': 'Sigmund Freud writes "Letter to an American Mother", urging compassion and tolerance for homosexuality. https://commons.wikimedia.org/wiki/File:A_Letter_from_Freud_to_a_mother_of_a_homosexual_-_1935_-_1.jpg',

    # 1940s
    '1945-04-01': 'The United States Holocaust Memorial Museum estimates 100,000 gay men were arrested and between 5,000 and 15,000 were placed in concentration camps. https://www.history.com/news/pink-triangle-nazi-concentration-camps',
    '1945-04-01': 'Just as Jews were forced to identify themselves with yellow stars, gay men in concentration camps had to wear a large pink triangle. https://www.history.com/news/pink-triangle-nazi-concentration-camps',

    '1945-02-20': 'First appearance of "bisexual" in the Congressional Record. https://ucsd.libguides.com/lgbtdocs/timeline',
    '1947-06-01': 'Lisa Ben publishes "Vice Versa", the earliest known US periodical published especially for lesbians. https://en.wikipedia.org/wiki/Vice_Versa_(magazine)',
    #'1948-03-01': 'Alfred Kinsey publishes "Sexual Behavior in the Human Male," concluding that homosexual behavior is not restricted to those identifying as homosexual and 37% of men have enjoyed homosexual activities at least once. https://www.pbs.org/wgbh/americanexperience/features/stonewall-milestones-american-gay-rights-movement/', # 54 characters too long / should be 287 max

    # 1950s
    '1950-11-11': 'The Mattachine Society was founded. https://en.wikipedia.org/wiki/Mattachine_Society',
    '1951-01-01': 'Roberta Cowell is the first known British trans woman to undergo reassignment surgery. https://en.wikipedia.org/wiki/Roberta_Cowell',
    '1952-01-12': 'Alan Turing was charged, trialed, and convicted with "gross indecency" for having a homosexual relationship with his partner, Arnold Murray. https://en.wikipedia.org/wiki/Alan_Turing#Conviction_for_indecency',
    '1952-12-01': 'Christine Jorgensen is the first trans American to undergo reassignment surgery. https://en.wikipedia.org/wiki/Christine_Jorgensen',
    '1955-09-21': 'The Daughters of Bilitis becomes the first lesbian rights organization in the United States. https://en.wikipedia.org/wiki/Daughters_of_Bilitis',
    '1955-12-20': 'Frank Kameny is fired from his job as an astronomer in the United States Army\'s Map Service in Washington, DC because of his homosexuality. Days later, he is denied from seeking federal employment. thelavendereffect.org/2013/12/20/december-20-in-lgbtq-history-2/',
    '1958-01-13': 'United States Supreme Court rules in favor of the First Amendment rights of the lesbian, gay, bisexual and transgender (LGBT) magazine One: The Homosexual Magazine. https://en.wikipedia.org/wiki/One,_Inc._v._Olesen',
    '1958-03-05': 'Tony Dyson writes a letter to the Times leading to the formation of the Homosexual Law Reform Society. A society that campaigned for the legalisation of same-sex relationships in the UK. https://en.wikipedia.org/wiki/Homosexual_Law_Reform_Society',

    # 1960s
    '1961-09-11': 'The first US-televised documentary about homosexuality airs on a local station in California. https://en.wikipedia.org/wiki/The_Rejected',
    '1962-01-01': 'Illinois repeals its sodomy laws, becoming the first U.S. state to decriminalize homosexuality. https://en.wikipedia.org/wiki/LGBT_rights_in_Illinois',
    '1966-04-21': 'The Mattachine Society organizes gay rights “Sip-In.” http://www.nytimes.com/2016/04/21/nyregion/before-the-stonewall-riots-there-was-the-sip-in.html',
    '1966-08-01': 'Compton\'s Cafeteria riots mark the beginning of the transgender activism in San Francisco. https://en.wikipedia.org/wiki/Compton%27s_Cafeteria_riot',
    '1969-06-27': 'Canada decriminalized homosexuality. https://en.wikipedia.org/wiki/Criminal_Law_Amendment_Act,_1968%E2%80%9369',
    '1969-06-28': 'Stonewall riots. https://en.wikipedia.org/wiki/Stonewall_riots',
    '1969-11-02': 'Craig Rodwell, his partner Fred Sargeant, Ellen Broidy, and Linda Rhodes proposed the first gay pride parade to be held in New York City. https://en.wikipedia.org/wiki/Pride_parade#:~:text=On%20November%202%2C%201969%2C%20Craig,ERCHO%20meeting%20in%20Philadelphia.',

    # 1970s
    '1970-06-28': 'Community members in New York City march through the streets to recognize the 1-yr anniversary of the Stonewall riots. This event is now considered the 1st gay pride parade. http://www.pbs.org/wgbh/americanexperience/features/timeline/stonewall/',
    '1972-01-01': 'In 1972, The Men with the Pink Triangle, the first autobiography of a gay concentration camp survivor, was published. https://www.history.com/news/pink-triangle-nazi-concentration-camps',
    '1973-01-01': 'Post-war Germany\'s first gay rights organization, Homosexuelle Aktion Westberlin (HAW), reclaimed the pink triangle as a symbol of liberation. nursingclio.org/2017/04/20/pink-triangle-legacies-holocaust-memory-and-international-gay-rights-activism/',
    '1972-07-01': 'The first Pride march is held in London, attracting around 2000 participants. https://www.bbc.com/news/uk-england-40533612',
    '1973-01-01': 'Maryland becomes the first state to statutorily ban same-sex marriage. https://www.npr.org/templates/story/story.php?storyId=5164355#:~:text=Maryland%20Judge%20Rejects%20Gay%2DMarriage%20Ban%20A%20Maryland%20circuit%20court,court%20has%20affirmed%20the%20decision.',
    '1973-03-11': 'First meeting of Parents and Friends of Gays. https://pflag.org/our-story#:~:text=The%20first%20formal%20meeting%20took,Approximately%2020%20people%20attended.',
    '1973-03-26': 'First meeting of "Parents and Friends of Gays," which goes national as Parents, Families and Friends of Lesbians and Gays (PFLAG) in 1982. https://pflag.org/our-story',
    '1973-10-31': '@LambdaLegal becomes the first legal organization established to fight for the equal rights of gays and lesbians.' 'https://www.lambdalegal.org/about-us/history',
    '1973-12-15': 'The board of the American Psychiatric Association votes to remove homosexuality from its list of mental illnesses. https://www.hrc.org/news/flashbackfriday-today-in-1973-the-apa-removed-homosexuality-from-list-of-me',
    '1974-04-02': 'Kathy Kozachenko becomes the first openly gay American elected to public office. https://www.nbcnews.com/feature/nbc-out/meet-lesbian-who-made-political-history-years-harvey-milk-n1174941',
    '1974-05-14': 'The Equality Act of 1974 prohibits discrimination "on the basis of sex, marital status, and sexual orientation, and for other purposes." https://ucsd.libguides.com/lgbtdocs/timeline',
    '1975-01-14': 'First federal gay rights bill is introduced to address discrimination based on sexual orientation (Civil Rights Amendments of 1975). https://www.congress.gov/bill/94th-congress/house-bill/166/all-info',
    '1977-06-28': 'The Front d\'Alliberament Gai de Catalunya calls the first LGBT Pride demonstration in Barcelona when homosexuality was still illegal in Spain. 5000 people participate. https://es.wikipedia.org/wiki/Diversidad_sexual_en_Espa%C3%B1a#El_siglo_XIX_y_principios_del_XX',
    '1977-11-08': 'Harvey Milk wins a seat on the San Francisco Board of Supervisors. https://en.wikipedia.org/wiki/Harvey_Milk',
    '1977-07-08': 'João W. Nery became the first Brazilian transgender to have undergone sex-change surgery in Brazil. https://en.wikipedia.org/wiki/Jo%C3%A3o_W._Nery',
    '1978-01-09': 'Harvey Milk is inaugurated as San Francisco city supervisor and is the first openly gay man to be elected to a political office in California. http://milkfoundation.org/about/harvey-milk-biography/',
    '1978-06-25': 'The rainbow flag becomes a universal symbol of hope for LGBTQ people around the world. https://www.cnn.com/style/article/pride-rainbow-flag-design-history/index.html#:~:text=The%20rainbow%20flag%2C%20which%20has,openly%20gay%20artist%20and%20activist.',
    '1979-05-21': 'Riots occur after Dan White receives lenient sentencing for murdering Harvey Milk and George Moscone. https://en.wikipedia.org/wiki/White_Night_riots',
    '1979-10-14': 'An estimated 75,000 people participate in the National March on Washington for Lesbian and Gay Rights. https://en.wikipedia.org/wiki/National_March_on_Washington_for_Lesbian_and_Gay_Rights',
    '1979-01-11': 'The law that decriminalizes homosexuality in Spain comes into force. https://es.wikipedia.org/wiki/Diversidad_sexual_en_Espa%C3%B1a#El_siglo_XIX_y_principios_del_XX',

    # 1980s
    '1981-02-05': 'Toronto police execute Operation Soap, raiding four gay bath houses. Community response regarded as Canadian equivalent of the 1969 Stonewall riots, evolving into Toronto Pride Week  https://en.wikipedia.org/wiki/Operation_Soap',
    '1982-03-02': 'Wisconsin becomes the first U.S. state to outlaw discrimination on the basis of sexual orientation. https://en.wikipedia.org/wiki/LGBT_rights_in_Wisconsin',
    '1988-12-01': 'The World Health Organization organizes the first World AIDS Day to raise awareness of the spreading pandemic. https://www.verywellhealth.com/the-history-of-world-aids-day-48717',
    '1989-10-01': 'Denmark becomes the first country to grant registered partnerships to same-sex unions. https://en.wikipedia.org/wiki/LGBT_rights_in_Denmark',

    # 1990s
    '1993-11-30': 'President Bill Clinton signs a military policy directive that prohibits openly gay and lesbian Americans from serving in the military but also prohibits the harassment of closeted homosexuals. https://www.cnn.com/2013/02/01/us/bill-clinton-fast-facts/index.html',
    '1996-01-01': 'A landmark case rules an employee who was about to transition was wrongfully dismissed. https://en.wikipedia.org/wiki/P_v_S_and_Cornwall_County_Council',
    '1996-03-12': "Five years after a gay couple filed suit against Hawaii for denying them a marriage license, Hawaiian state court upheld the right of same-sex couples to be legally wed. This made Hawaii the first state to legalize gay marriage cnn.com/US/9612/03/same.sex.marriage",
    '1997-04-14': 'Comedian Ellen DeGeneres comes out as a lesbian on the cover of Time magazine. http://content.time.com/time/covers/0,16641,19970414,00.html',
    '1997-04-30': "DeGeneres' character, Ellen Morgan, on her self-titled TV series 'Ellen' becomes the first leading character to come out on a prime-time network television show. https://en.wikipedia.org/wiki/Ellen_(TV_series)",
    '1997-12-18': 'In New Jersey, same-sex couples are given the right to jointly adopt children. https://www.washingtonpost.com/archive/politics/1997/12/18/nj-allows-gays-to-adopt-jointly/7b031fcd-1338-4dff-b548-1e54eb196f12/',
    '1998-04-01': 'Martin Luther King Jr.\'s widow, Coretta Scott King, asks the civil rights community to help in the effort to extinguish homophobia. https://www.cnn.com/2013/08/23/us/coretta-scott-king-fast-facts/index.html',

    # 2000s
    '2000-12-08': 'The Bundestag officially apologizes to gays and lesbians persecuted under the Nazi regime, and for "harm done to homosexual citizens up to 1969". https://en.wikipedia.org/wiki/LGBT_history_in_Germany',
    '2001-04-01': 'The Netherlands became the first country to legalize same-sex marriages. https://en.wikipedia.org/wiki/Same-sex_marriage_in_the_Netherlands',
    '2004-05-17': 'The first legal same-sex marriage in the United States takes place in Massachusetts. https://www.npr.org/2019/05/17/723649385/the-1st-legally-married-same-sex-couple-wanted-to-lead-by-example',
    '2004-07-20': 'Guido Westerwelle, leader of the FDP, becomes the first leader of a major party to come out. https://en.wikipedia.org/wiki/LGBT_history_in_Germany',
    '2005-07-03': 'Same-sex marriage becomes legal in Spain. https://es.wikipedia.org/wiki/Matrimonio_entre_personas_del_mismo_sexo_en_Espa%C3%B1a',
    '2005-07-20': 'The enactment of the Civil Marriage Act allows same-sex couples to be married anywhere in Canada. http://laws-lois.justice.gc.ca/eng/acts/c-31.5/page-1.html',
    '2005-09-06': 'The California legislature becomes the first to pass a bill allowing marriage between same-sex couples. Governor Arnold Schwarzenegger vetoes the bill. https://www.nytimes.com/2005/09/06/national/california-legislature-approves-samesex-marriage-bill.html',
    '2005-12-05': 'The Civil Partnership Act passes, granting civil partnership in the UK. https://en.wikipedia.org/wiki/Civil_Partnership_Act_2004',
    '2006-10-25': 'The New Jersey Supreme Court rules that state lawmakers must provide the rights and benefits of marriage to gay and lesbian couples. https://www.cnn.com/2006/US/10/25/gay.marriage/',
    '2007-12-21': 'Homosexuality was legalized in Nepal in 2007. https://en.wikipedia.org/wiki/LGBT_rights_in_Nepal',
    '2008-01-20': 'Uruguay became the first Latin American country to enact a national same-sex civil union law. https://en.wikipedia.org/wiki/Same-sex_marriage_in_Uruguay',
    '2008-05-15': 'The California Supreme Court rules in reMarriage Cases that limiting marriage to opposite-sex couples is unconstitutional. https://www.aclunc.org/our-work/legal-docket/re-marriage-cases',
    '2008-11-04': 'Voters approve Proposition 8 in California, which makes same-sex marriage illegal. The proposition is later found to be unconstitutional by a federal judge. https://en.wikipedia.org/wiki/2008_California_Proposition_8',
    '2009-06-11': 'LGBT persons in Botswana face legal issues not experienced by non-LGBT citizens. Same-sex sexual acts have been legal in Botswana since 11 June 2019 after a unanimous ruling by the High Court of Botswana. https://en.m.wikipedia.org/wiki/LGBT_rights_in_Botswana',
    '2009-04-03': 'Same-sex marriage is legal in the state of Iowa. https://en.wikipedia.org/wiki/Same-sex_marriage_in_Iowa',
    '2009-05-15': 'Westerwelle becomes the first openly gay member of the Federal Cabinet (Vice Chancellor and Foreign Minister under Angela Merkel coalition government). https://en.wikipedia.org/wiki/LGBT_history_in_Germany',
    '2009-05-16': 'The first monument dedicated to remembering the persecution of homosexuals during the Franco regime is inaugurated in Durango, Spain. https://es.wikipedia.org/wiki/Diversidad_sexual_en_Espa%C3%B1a#El_siglo_XIX_y_principios_del_XX',
    '2009-10-17': 'Changing legal gender assignment in Brazil is legal according to the Superior Court of Justice of Brazil. https://en.wikipedia.org/wiki/Transgender_rights_in_Brazil#:~:text=The%20Supreme%20Federal%20Court%20ruled,declaration%20of%20their%20psychosocial%20identity.',

    # 2010s
    '2010-02-10': 'France becomes the first conutry to declassify gender indentity disorder as a mental illness. https://www.loc.gov/law/foreign-news/article/france-gender-identity-disorder-dropped-from-list-of-mental-illnesses/',
    '2010-07-15': 'Argentina legalises gay marriage. https://www.thehindu.com/news/international/Argentina-legalises-gay-marriage/article16197744.ece',
    '2011-05-05': 'Same-sex stable union is now legal in Brazil. https://en.wikipedia.org/wiki/LGBT_rights_in_Brazil',
    '2011-09-20': 'Repeal of DADT. https://www.americanprogress.org/issues/lgbtq-rights/reports/2012/09/20/38764/the-repeal-of-dont-ask-dont-tell-1-year-later/',
    '2012-05-09': 'In an ABC interview, Obama becomes the first sitting US president to publicly support the freedom for LGBTQ couples to marry. https://www.cnn.com/2012/05/09/politics/obama-same-sex-marriage/',
    '2012-06-15': 'Same-sex marriage became legal in Denmark. https://en.wikipedia.org/wiki/LGBT_rights_in_Denmark#Recognition_of_same-sex_relationships',
    '2012-09-30': 'California bans gay "conversion" therapy for minors. https://www.reuters.com/article/us-california-gaytherapy-idUSBRE88T0DR20120930',
    '2012-11-06': 'Tammy Baldwin becomes the first openly gay politician and the first Wisconsin woman to be elected to the US Senate. https://www.cnn.com/2012/11/07/politics/wisconsin-tammy-baldwin-senate/',
    '2013-05-16': 'Although same-sex unions have been legalized since 2004 in Brazil, only since 2013 is same-sex marriage legal. https://en.wikipedia.org/wiki/Same-sex_marriage_in_Brazil',
    '2013-06-26': 'Repeal of DOMA. https://www.americanprogress.org/issues/immigration/news/2013/06/26/68033/what-the-doma-decision-means-for-lgbt-binational-couples/',
    '2013-08-05': 'Uruguay became the twelfth country in the world to legalize gay marriage and the second Latin American country, after Argentina. https://www.bbc.com/news/world-latin-america-23571197',
    '2013-10-24': 'As a less exclusive alternative to "LGBT," "LGBTQ," and "LGBTQIA+," the acronym "GSRM," which stands for "Gender, Sexual, and Romantic Minorities", has been added to Urban Dictionary. ',
    '2014-02-09': 'Michael Sam becomes the first openly gay football player in the NFL. https://www.espn.com/espn/otl/story/_/id/10429030/michael-sam-missouri-tigers-says-gay',
    '2014-03-13': 'The Marriage (Same Sex Couples) Act 2013 (c. 30) introduced same-sex marriage in England and Wales. https://en.wikipedia.org/wiki/Marriage_(Same_Sex_Couples)_Act_2013#13_March_2014:_Same-Sex_Marriage',
    '2014-04-05': 'Indian Supreme court recognises transgender people as third gender. https://www.bbc.com/news/world-asia-india-27031180',
    '2014-06-03': 'British Indian Ocean Territory legalizes same sex marriage. https://en.wikipedia.org/wiki/Recognition_of_same-sex_unions_in_the_British_Overseas_Territories',
    '2015-06-09': 'Secretary of Defense Ash Carter announces that the Military Equal Opportunity policy has been adjusted to include gay and lesbian military members. https://www.cnn.com/2015/06/09/politics/carter-sexual-orientation-policy/index.html',
    '2015-06-26': 'The Supreme Court finally and officially declared same-sex marriage a Constitutional right nationwide. https://www.nytimes.com/2015/06/27/us/supreme-court-same-sex-marriage.html',
    '2015-07-23': 'The military allows transgender Americans to serve openly in the military. https://www.advocate.com/politics/military/2015/07/13/reports-pentagon-poised-lift-transgender-military-ban',
    '2015-07-23': 'The Equality Act is introduced. https://en.wikipedia.org/wiki/Equality_Act_United_States',
    '2015-07-27': 'Boy Scouts of America President Robert Gates announces, "the national executive board ratified a resolution removing the national restriction on openly gay leaders and employees." https://www.cnn.com/2015/07/27/us/boy-scouts-gay-leaders-feat/',
    '2015-11-12': 'Indian MP Shashi Tharoor introduced a bill to decriminalize homosexuality, but it was rejected by the Lok Sabha. https://www.deccanherald.com/specials/history-of-the-pride-movement-in-india-742950.html',
    '2016-05-17': 'The Senate confirms Eric Fanning to be secretary of the Army, making him the first openly gay secretary of a US military branch. https://www.cnn.com/2016/05/17/politics/eric-fanning-secretary-of-the-army/',
    '2016-06-24': 'Obama announces the designation of the first national monument to lesbian, gay, bisexual and transgender LGBTQ rights. https://obamawhitehouse.archives.gov/blog/2016/06/24/president-obama-designates-stonewall-national-monument',
    '2016-06-30': 'Secretary of Defense Carter announces that the Pentagon is lifting the ban on transgender people serving openly in the US military. https://www.cnn.com/2016/06/30/politics/transgender-ban-lifted-us-military/',
    '2016-08-05': 'There were a record number of "out" athletes in Summer Olympic Games in Rio de Janeiro. @HRC estimates there were at least 41 openly lesbian, gay and bisexual Olympians -- up from 23 in London 2012 olympics. edition.cnn.com/2016/08/11/sport/rio-2016-lgbt-olympians',
    '2016-09-16': 'Lilly Singh became the first late-night host to ever publicly identify as bisexual. https://en.wikipedia.org/wiki/A_Little_Late_with_Lilly_Singh',
    #'2016-11-09': 'Kate Brown is sworn in as governor of Oregon, a day after she was officially elected to the office. Brown becomes the highest-ranking LGBTQ person elected to office in the United States. npr.org/sections/thetwo-way/2016/11/09/501338927/for-first-time-openly-lgbt-governor-elected-oregons-kate-brown', # 34 characters too long / should be 287 max
    '2016-12-30': 'India opens first school for transgender pupils in the city of Kochi. https://www.bbc.com/news/world-asia-india-38470192',
    '2017-06-27': 'District of Columbia residents can now choose a gender-neutral option on their driver\'s license. https://www.cnn.com/2017/06/27/health/washington-gender-neutral-drivers-license/index.html',
    #'2017-11-07': 'Virginia voters elect the state\'s first openly transgender candidate to the Virginia House of Delegates. Danica Roem unseats incumbent delegate Bob Marshall, who had been elected 13 times over 26 years. cnn.com/2017/11/07/politics/danica-roem-virginia-transgender/index.html', # 10 characters too long / should be 287 max
    '2017-12-09': 'On this day Australia legalised same-sex marriage. https://en.wikipedia.org/wiki/LGBT_rights_in_Australia',
    '2018-02-26': 'The Pentagon confirms that the first transgender person has signed a contract to join the US military. https://www.cnn.com/2018/02/26/politics/first-transgender-recruit-join-us-military/index.html',
    '2018-03-01': 'Transgender folks have the right to change their official name & sex without the need of surgery or professional evaluation in Brazil. en.wikipedia.org/wiki/Transgender_rights_in_Brazil',
    '2018-03-23': 'The Trump administration announces a new policy that bans transgender people from serving in the military. After several court battles, the Supreme Court allows the ban to go into effect in January 2019 cnn.com/2018/03/23/politics/transgender-white-house/index.html',
    '2018-09-06': 'The Supreme Court of India decriminalized Section 377 making gay sex legal. https://timesofindia.indiatimes.com/topic/same-sex-marriage',
    '2018-11-06': 'Democratic US Representative Jared Polis wins the Colorado governor\'s race, becoming the nation\'s first openly gay man to be elected governor. https://www.cnn.com/2018/11/06/politics/jared-polis-colorado-gay-governor/index.html',
    '2019-02-16': 'Nyla Rose became the first openly transgender wrestler in history to sign with a major American promotion. https://en.wikipedia.org/wiki/Nyla_Rose',
    '2019-04-02': 'Lori Lightfoot was elected Chicago, Illinois first openly gay mayor. https://www.nbcnews.com/news/us-news/lori-lightfoot-elected-chicago-mayor-will-be-1st-black-woman-n990266',
    '2019-05-17': 'Same-sex marriage was legalized in Taiwan and became effective since 24 May 2019, including rights in areas such as taxes, insurance, and child custody. https://en.wikipedia.org/wiki/LGBT_history_in_Taiwan',
    '2019-05-25': 'Transgender no longer recognized as "disorder" by WHO. https://time.com/5596845/world-health-organization-transgender-identity/',
    '2019-06-13': 'Discrimination on the basis of sexual orientation and gender identity became a crime in Brazil. https://en.wikipedia.org/wiki/LGBT_rights_in_Brazil',
    '2018-06-18': 'WHO no longer classifies being transgender as a mental illness. https://eu.usatoday.com/story/news/2018/06/20/transgender-not-mental-illness-world-health-organization/717758002/',
    '2019-09-22': 'Billy Porter becomes the first openly gay black man to win the Emmy for best lead actor in a drama series. https://www.cnn.com/2019/09/22/entertainment/billy-porter-first-openly-gay-black-actor-emmy/index.html',
    '2019-09-25': 'Angelica Ross became the first openly transgender person to host an American presidential forum. https://en.wikipedia.org/wiki/Angelica_Ross',
    '2019-11-08': 'Kerala hosts India\'s first-ever trans art festival. https://www.newindianexpress.com/states/kerala/2019/sep/20/kerala-to-host-indias-first-ever-trans-art-festival-2036485.html',
    '2019-12-18': 'Conversion therapy is completely banned for minors and partially banned for adults in December 2019. https://en.wikipedia.org/wiki/LGBT_history_in_Germany',

    # 2020s
    '2020-02-12': 'New Jersey residents can now change the gender marker on a driver\'s license without a note from a doctor. https://www.northjersey.com/story/news/new-jersey/2020/02/12/nj-mvc-allow-gender-designation-changes-without-doctors-note/4738926002/',
    '2020-05-08': 'Maryland repealed it\'s sodomy law. https://www.billtrack50.com/BillDetail/1166637',
    '2020-05-26': 'Costa Rica becomes the first country in Central America to legalize same-sex marriage. https://www.cnn.com/2020/05/26/americas/costa-rica-legalizes-same-sex-marriage-trnd/index.html',
    '2020-06-15': 'The Supreme Court rules that federal law protects LGBTQ workers from discrimination. https://www.cnn.com/2020/06/15/politics/supreme-court-lgbtq-employment-case/index.html',
    '2020-07-16': 'Sudan abolished the death penalty and flogging for homosexuality. https://www.reuters.com/article/us-sudan-lgbt-rights-trfn/great-first-step-as-sudan-lifts-death-penalty-and-flogging-for-gay-sex-idUSKCN24H30J',
    '2020-09-15': 'India\'s most populated state, Uttar Pradesh approves setting up of a transgender welfare board in the state. https://indianexpress.com/article/cities/lucknow/up-minister-shastri-approves-setting-up-of-transgender-welfare-board-in-state-6597718/',
    '2020-10-01': 'Petra De Sutter becomes Europe\'s first transgender deputy prime minister, and the most senior trans politician in Europe. https://www.reuters.com/article/idUSL8N2GS6EL',
    '2020-10-21': 'Pope Francis expresses support for same-sex civil unions, marking one of the first occassions the Roman Catholic Church has spoken in recognition of LGBTQ people https://www.nytimes.com/2020/10/21/world/europe/pope-francis-same-sex-civil-unions.html',
}

# NOTE: must fit in a tweet, so not longer than this line or max of 287 characters ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|