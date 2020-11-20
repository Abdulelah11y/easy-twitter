# required libraries
import tweepy
import pandas as pd
import numpy as np




consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def connect_me():

    '''
    To establish the connection with Twitter

    '''

    global consumer_key
    consumer_key = input('Enter your consumer key: ')
    global consumer_secret
    consumer_secret = input('Enter your consumer secret: ')
    global access_token
    access_token = input('Enter your access token: ')
    global access_token_secret
    access_token_secret = input('Enter your access token secret: ')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    test_account = "bassammutairi"

    try:
        api.user_timeline(test_account)
        print('You are good to go!')
    except:
        print('Please enter valid keys!')


def get_user_timeline():

    '''
    returns a summary about the latest 20 tweets of a specific twitter account

    '''
    dataframe = []

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    twitter_account = input('Enter twitter account: ')
    tweets = api.user_timeline(twitter_account)

    for tweet in tweets:
        dataframe.append(tweet.text)

    df = pd.DataFrame(dataframe, columns=['tweets'])

    # We add relevant data:
    df['len']  = np.array([len(tweet.text) for tweet in tweets])
    df['ID']   = np.array([tweet.id for tweet in tweets])
    df['Date'] = np.array([tweet.created_at for tweet in tweets])
    df['Source'] = np.array([tweet.source for tweet in tweets])
    df['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    df['RTs']    = np.array([tweet.retweet_count for tweet in tweets])

    return df


def get_followers_details():

    '''
    return details about a specific twitter account's followers

    '''
    import json
    import os

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    twitter_account = input('Enter twitter account: ')
    tweet_ids = api.followers(twitter_account)

    count = 0

    with open('tweet_json.txt', 'w') as outfile:
        for tweet_id in tweet_ids:
            count += 1
            try:
                json.dump(tweet_id._json, outfile)
                outfile.write('\n')
            except tweepy.TweepError as e:
                fails_dict[tweet_id] = e
                pass

    tweets = []
    with open('tweet_json.txt') as file:
        for eachline in file:
            try:
                tweet = json.loads(eachline)
                tweets.append(tweet)
            except:
                continue

    os.remove("tweet_json.txt")
    dataframe = pd.DataFrame(tweets, columns=list(tweets[0].keys()))
    return dataframe
