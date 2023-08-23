# c6LSXawfQm3iGSNTqL7LnRYqU - c K
# 6Z2VT0vXe2SOhZV6o4vPNstWQeo4TrSApyHNyRMhDJOBdbIgg9 - c s k
# 1235133935044014080-FIpuSnyJb1TTQK6gOMxbCp9NteDIYz - access token
# flM4YOg0G6pxhHDhm2KtubD3j0UXOHISWonY96mJSyygX - access secret token


import tweepy

# Your Twitter API credentials
consumer_key = 'c6LSXawfQm3iGSNTqL7LnRYqU'#"consumer_key"
consumer_secret = '6Z2VT0vXe2SOhZV6o4vPNstWQeo4TrSApyHNyRMhDJOBdbIgg9'#"consumer_secret"
access_token = '1235133935044014080-suHiffNHsUCJfRTkxPgphY6p7vtk7R'#"access_token"
access_token_secret = 'HQCoxSaSuQLTmw0pqAFnX8T8Bd5KDaV7VqR17XG9oGADh'#"access_token_secret"

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