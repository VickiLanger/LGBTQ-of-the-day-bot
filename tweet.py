'''
tweet.py: post tweets to twitter.com
11 September 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
import time
import random

from os import environ, remove

from get_tweet_content import get_tweet_content
from get_img_for_tweet import get_img_for_tweet
from get_reply import get_reply


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
    except Exception as error:
        print(f"An error occurred when attempting to authenticate with the twitter API. reason: {error}")


def main():
    api = authenticate_api()

    # choose tweet

    print("finding a tweet...")
    tweet_content = get_tweet_content()
    print("chose tweet: " + tweet_content["text"])

    try:
        # obtain image
        image_path = get_img_for_tweet(tweet_content["text"])

        # prepare image
        image = api.media_upload(image_path)
        # add alt-text
        api.create_media_metadata(
            media_id=image.media_id, alt_text=tweet_content["text"])
    except Exception as error:
        print(f"An error occurred while generating image. reason: {error}")

    # Post tweet
    tweet = api.update_status(status=tweet_content["text"],
                              media_ids=[image.media_id])  # variable used later for reply to this tweet
    print('tweet has been tweeted')

    # delete image once posted
    remove(image_path)

    # Reply to tweet
    # Get reply
    reply_with = get_reply(tweet_content["label"])

    # Check if a reply was returned
    if (reply_with):
        api.update_status(status=reply_with, in_reply_to_status_id=tweet.id,
                          auto_populate_reply_metadata=True)
        print('chose reply:' + reply_with)
        print('reply has been tweeted')
    else:
        print(f"Don't have a definition for {tweet_content['label']}")


if __name__ == "__main__":
    main()