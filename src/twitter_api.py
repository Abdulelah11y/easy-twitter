import tweepy
import pandas as pd

def get_user_timeline():
    
    ''' returns timeline about a specific twitter account '''

    dataframe = []
    consumer_key = input('Enter your consumer key: ')
    consumer_secret = input('Enter your consumer secret: ')
    access_token = input('Enter your access token: ')
    access_token_secret = input('Enter your access token secret: ')
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    twitter_account = input('Enter twitter account: ')
    user_timeline = api.user_timeline(twitter_account)
    for tweet in user_timeline:
        dataframe.append(tweet.text)

    df = pd.DataFrame(dataframe)
    return df