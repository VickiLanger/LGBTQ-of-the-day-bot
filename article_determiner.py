import re
def get_indefinite_article(adjective):
    '''
    Algorithm adapted from CPAN package Lingua-EN-Inflect-1.891 by Damian Conway.
    Takes a string parameter adjective as input.
    Returns a unicode string "a" or "an" 
    '''
    m = re.search('\w+', adjective, re.UNICODE)

    if m:
        word = m.group(0)
    else:
        return u'an'

    wordi = word.lower()
    for anword in ('euler', 'heir', 'honest', 'hono'):
        if wordi.startswith(anword):
            return u'an'

    if wordi.startswith('hour') and not wordi.startswith('houri'):
        return u'an'

    if len(word) == 1:
        if wordi in 'aedhilmnorsx':
            return u'an'
        else:
            return u'a'

    if re.match(r'(?!FJO|[HLMNS]Y.|RY[EO]|SQU|'
                  r'(F[LR]?|[HL]|MN?|N|RH?|S[CHKLMNPTVW]?|X(YL)?)[AEIOU])'
                  r'[FHLMNRSX][A-Z]', word):
        return u'an'

    for regex in (r'^e[uw]', r'^onc?e\b',
                    r'^uni([^nmd]|mo)','^u[bcfhjkqrst][aeiou]'):
        if re.match(regex, wordi):
            return u'a'

    if re.match('^U[NK][AIEO]', word):
        return u'a'
    elif word == word.upper():
        if wordi[0] in 'aedhilmnorsx':
            return u'an'
        else:
            return u'a'

    if wordi[0] in 'aeiou':
        return u'an'

    if re.match(r'^y(b[lor]|cl[ea]|fere|gg|p[ios]|rou|tt)', wordi):
        return u'an'

    else:
        return u'a'

''' Testing with various strings
if __name__ == "__main__": 
    print(indefinite_article("honest")) - an
    print(indefinite_article("utensil")) - a
    print(indefinite_article("unicorn")) - a
    print(indefinite_article("Apple")) - an
    print(indefinite_article("year")) - a
'''
