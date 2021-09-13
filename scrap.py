import tweepy

import os

# Authorization to consumer key and consumer secret
auth = tweepy.OAuthHandler('v7BkBsTkUONWDEfOUmoii46PW', 'rlt60otzfQJNxkr1wMwon3Q1MfhdHFz5YUkKCCGm3vWA8LT6MG')
	
# Access to user's access key and access secret
# auth.set_access_token('c1264944667470319616-y8wwtzsAi4HmcYxBU4294HbVyTZh7V', 'GvP1CJdoDq9ATM8bcJmf892rafaxomiTAvZn119UalYex')

# Calling api
api = tweepy.API(auth)

# # 200 tweets to be extracted
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

for tweet in tweepy.Cursor(api.search, q='#vaccine').items(10):
    print(tweet.text)