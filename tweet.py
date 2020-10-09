'''
tweet.py: post tweets to twitter.com
11 September 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
# import time
import random 

import os

from get_tweet import get_tweet
# from get_reply import get_reply


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


def get_img_random():
    no=0
    while(True):
        no = random.randint(0,99)
        if(os.path.exists('post_'+str(no)+'.png')):
            return 'post_'+str(no)+'.png'
        else:
            continue
            
            
def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
    except Exception as error:
        print(f"An error occurred when attempting to authenticate with the twitter API. reason: {error}")



def main():
    api = authenticate_api()
    #reply_with = get_reply()

    # print("finding a tweet...")
    # tweet = get_tweet()
    # print("chose tweet: " + tweet)
    
    #get_tweet() is now done by generateImagePost.py, so the above won't be required
    
    #To choose a random image file name:
    img = get_img_random()
    
    #To just upload the selected image to Twitter:
    tweet = api.update_with_media(img)  # variable used later for reply to this tweet
    print('tweet has been tweeted')
    #api.update_status(status=reply_with, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    #print('chose reply:' + reply_with)
    #print('reply has been tweeted')


main()
