import random

import requests
import json

random_num = random.randint(100, 9999)
random_num = str(random_num)


payload1 = json.dumps({
    "text": "#STEPINSUMMIT2023 S&P Ratings" + random_num + " @stepin_fourm@veritfy_software"
})

payload2 = json.dumps({
    "text": "#TESTAUTOTHON2023 #STEPINSUMMIT2023" + random_num + "@stepin_fourm@veritfy_software"
})

url = "https://api.twitter.com/2/tweets"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'OAuth oauth_consumer_key="JhUC1TwlzzWIbYgZH4huCHt8d",'
                   'oauth_token="1235133935044014080-GTXl65ApuI5ZfavndAx6phjRLU0uvX",'
                   'oauth_signature_method="HMAC-SHA1",oauth_timestamp="1692787382",oauth_nonce="vBSMi89sOOX",'
                   'oauth_version="1.0",oauth_signature="ZXhMflf4vsJrZY4T%2B0iRfzN3d2U%3D"',
  'Cookie': 'guest_id=v1%3A169276455289286362'
}

response1 = requests.request("POST", url, headers=headers, data=payload1)

response2 = requests.request("POST", url, headers=headers, data=payload2)

print(response1.text)

print(response2.text)
