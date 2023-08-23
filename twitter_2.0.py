import requests
import json

# Replace with your actual Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGczpgEAAAAAqOakfljLYdlrPOo47ukLxuzkljs%3Dl8eKEeUB28hkt3gCtaUZZtUw7S8BIuzyZGPjKlcqC5hdxwRg7F"

# API endpoint for posting tweets
tweet_url = "https://api.twitter.com/2/tweets"

# Your tweet content
tweet_content = "#TESTAUTOTHON2023 - YES WE DID IT ...."

headers = {
   "Authorization": f"Bearer {bearer_token}",
   "Content-Type": "application/json"
}

data = {
   "text": tweet_content
}

response = requests.post(tweet_url, headers=headers, data=json.dumps(data))

if response.status_code == 201:
   print("Tweet posted successfully!")
else:
   print("Error posting tweet:", response.text)
