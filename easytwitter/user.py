# required libraries
import tweepy
import pandas as pd






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
    returns latest 20 tweets of a specific twitter account timeline

    '''
    dataframe = []

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    twitter_account = input('Enter twitter account: ')
    user_timeline = api.user_timeline(twitter_account)
    for tweet in user_timeline:
        dataframe.append(tweet.text)

    df = pd.DataFrame(dataframe)
    return df

def get_followers_details():

    '''
    return details about a specific twitter account's followers

    '''
    import json


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    twitter_account = input('Enter twitter account: ')

    df = api.followers(twitter_account)

    tweets = []
    for eachline in df:
        try:
            tweet = json.loads(eachline)
            tweets.append(tweet)
        except:
            continue
    dataframe = pd.DataFrame(tweets, columns=list(tweets[0].keys()))
    return dataframe
