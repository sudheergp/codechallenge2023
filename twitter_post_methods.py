
from urllib.parse import parse_qsl
import requests
from requests_oauthlib import OAuth1
import tweepy


# Twitter API credentials
consumer_key = 'gUb5DQ0Sgc5Hm4aYIgcEmc1pU'#"consumer_key"
consumer_secret = 'TUkwt0sTMIShQ4KsHSt3QgrSIbeGuOs1GLlIe6dH3ggHnSxNww'#"consumer_secret"

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

