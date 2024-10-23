import tweepy
import requests

key = 'BYuDoqckMMrrhfSrr1uexF5cE'
k_secret = '2rSl4wyv2VnkWf5T1DSqcG2XOiy4NtD9Bt8P9RJVDXYiV8r95x'
bearer = 'AAAAAAAAAAAAAAAAAAAAAFztigAAAAAAwynrdTVJgeV9BLNseEDMamvk3lw%3DHTHgOAFnjfnpiyKJ9a59ZHg8jJb6wuBjNOAshJEXI1dj6jTMRK'
access = '427778635-oKS5nP2KtdsroNSYQnaWnFcgZCJhOBIQH2roO7zk'
a_secret = 'flRJnliGcH6OE6qOVOtFZGvS2x1XVWe6nqjg6UDb6Bbch'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(key, k_secret)
auth.set_access_token(access, a_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")

