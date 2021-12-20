import numpy as np
import json
import os
import tweepy
import pandas as pd
from easytwitter.auth import Auth


class Api:
    def get_user_timeline(self):
        '''
        returns a summary about the latest 20 tweets of a specific twitter account

        '''

        dataframe = []

        api = Auth.connect(self)
        if api != None:

            twitter_account = input('Enter twitter account: ')
            tweets = api.user_timeline(twitter_account)

            for tweet in tweets:
                dataframe.append(tweet.text)

            df = pd.DataFrame(dataframe, columns=['tweets'])

            # add relevant data:
            df['len'] = np.array([len(tweet.text) for tweet in tweets])
            df['ID'] = np.array([tweet.id for tweet in tweets])
            df['Date'] = np.array([tweet.created_at for tweet in tweets])
            df['Source'] = np.array([tweet.source for tweet in tweets])
            df['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
            df['RTs'] = np.array([tweet.retweet_count for tweet in tweets])

            print(df)
            return df
        else:
            print("You are not authorized.")

    def get_followers_details(self):
        '''
        return details about a specific twitter account's followers

        '''
        api = Auth.connect(self)
        if api != None:

            twitter_account = input('Enter twitter account: ')
            tweet_ids = api.followers(twitter_account)

            count = 0
            fails_dict = []
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

            print(dataframe)
            return dataframe
        else:
            print("You are not authorized.")


def main():
    # api = Api()
    # api.get_user_timeline()
    # api.get_followers_details()
    pass
