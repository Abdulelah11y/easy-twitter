import tweepy
from easytwitter.token import Token


class Auth():

    def connect(self):
        '''
        To establish the connection with Twitter

        '''
        if Token.AUTHORIZED == False:

            Token.CONSUMER_KEY = input('Enter your consumer key: ')
            Token.CONSUMER_SECRET = input('Enter your consumer secret: ')
            Token.ACCESS_TOKEN = input('Enter your access token: ')
            Token.ACCESS_TOKEN_SECRET = input(
                'Enter your access token secret: ')

        auth = tweepy.OAuthHandler(Token.CONSUMER_KEY, Token.CONSUMER_SECRET)
        auth.set_access_token(Token.ACCESS_TOKEN, Token.ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth)

        test_account = "twitter"

        try:
            api.user_timeline(test_account)
            Token.AUTHORIZED = True
            return api
        except:
            return None
