
from urllib.parse import parse_qsl
import requests
from requests_oauthlib import OAuth1
import tweepy


# Twitter API credentials
consumer_key = 'c6LSXawfQm3iGSNTqL7LnRYqU'#"consumer_key"
consumer_secret = '6Z2VT0vXe2SOhZV6o4vPNstWQeo4TrSApyHNyRMhDJOBdbIgg9'#"consumer_secret"

# Step 1: Get a request token
request_token_url = "https://api.twitter.com/oauth/request_token"
auth = OAuth1(consumer_key, consumer_secret)
response = requests.post(url=request_token_url, auth=auth)
request_token_data = dict(parse_qsl(response.text))

# Step 2: Redirect user to authorization URL
authorize_url = f"https://api.twitter.com/oauth/authorize?oauth_token={request_token_data['oauth_token']}"
print("Please visit this URL to authorize the app:", authorize_url)
oauth_verifier = input("Enter the OAuth verifier: ")

# Step 3: Get an access token
access_token_url = "https://api.twitter.com/oauth/access_token"
auth = OAuth1(consumer_key, consumer_secret, request_token_data['oauth_token'], request_token_data['oauth_token_secret'])
response = requests.post(url=access_token_url, auth=auth, params={'oauth_verifier': oauth_verifier})
access_token_data = dict(parse_qsl(response.text))

# Print the access token and secret (these are your write access credentials)
print("Access token:", access_token_data['oauth_token'])
print("Access token secret:", access_token_data['oauth_token_secret'])
#---------------------------------------------------------
# Twitter API Tokens
access_token = access_token_data['oauth_token']#"access_token"
access_token_secret = access_token_data['oauth_token_secret']#"access_token_secret"

# Create an OAuth 1.0a authentication handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Post a tweet
tweet_text = "#TESTAUTOTHON2023"
api.update_status(status=tweet_text)

# Make an API call using the authenticated API object
user = api.get_user(screen_name="sgandlapalli")
print(user.screen_name)
print(user.followers_count)




#------------------------------------------------------------------------------------------

# c6LSXawfQm3iGSNTqL7LnRYqU - c K
# 6Z2VT0vXe2SOhZV6o4vPNstWQeo4TrSApyHNyRMhDJOBdbIgg9 - c s k
# 1235133935044014080-FIpuSnyJb1TTQK6gOMxbCp9NteDIYz - access token
# flM4YOg0G6pxhHDhm2KtubD3j0UXOHISWonY96mJSyygX - access secret token


import tweepy

# Your Twitter API credentials
consumer_key = 'c6LSXawfQm3iGSNTqL7LnRYqU'#"consumer_key"
consumer_secret = '6Z2VT0vXe2SOhZV6o4vPNstWQeo4TrSApyHNyRMhDJOBdbIgg9'#"consumer_secret"
access_token = '1694278157556469763-LtLuMpkvyl37BtXIvSow29nHi3uI1u'#"access_token"
access_token_secret = 'nH14aDIh1LmVrhZNwwuM7lCceDQV6lXLgcryfcc434kro'#"access_token_secret"

# Create an OAuth 1.0a authentication handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Post a tweet
tweet_text = "#TESTAUTOTHON2023"
api.update_status(status=tweet_text)

# Make an API call using the authenticated API object
user = api.get_user(screen_name="omprakesh138748")
print(user.screen_name)
print(user.followers_count)


