from random import choice

from words_dir.tweet_nouns import nouns
from words_dir.tweet_adjectives import adjectives
from words_dir.tweet_labels import labels

from article_determiner import get_indefinite_article


def get_tweet_content():
    adjective = choice(adjectives)
    label = choice(list(labels.keys()))
    noun = choice(nouns)
    article = get_indefinite_article(adjective)

    tweet_text = f"today's queerness is {article} {adjective} {label} {noun}"

    return {
        'text': tweet_text,
        'label': label
    }
