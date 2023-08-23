
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







-------------------------------------------------------------------------------------------------
import requests
import json
import logging

api = requests
logger1 = logging.getLogger('')
class apirest:


    def get_user_credentials(self, **kwargs):
        """
        Description: This method is used to receive username and password\n
        :param kwargs: Username & Password argument should be passed like mentioned below also Password should be encrypted\n
                       (username="******", password="******")\n
        :return: Returns username and password\n

        NOTE: THIS IS AN INTERNAL METHOD
        """
        try:
            _authentication = None
            if ("username" and "password" in kwargs) and (
                    kwargs["username"] is not None and kwargs["password"] is not None):
                _authentication = (kwargs["username"],kwargs["password"])
        except:
            _authentication = None
        return _authentication

    def get_proxies(self, **kwargs):
        """
        Description: This method is used to receive proxies\n
        :param kwargs: Proxies argument should be passed like mentioned below\n
                       (proxies="YES" or proxies="NOT")\n
        :return: Returns proxies\n

        NOTE: THIS IS AN INTERNAL METHOD
        """
        try:
            proxies = None
            if "proxies" in kwargs:
                if "YES" in kwargs["proxies"].upper():
                    proxies = {
                        "http": None,
                        "https": None,
                    }
                elif "NOT" in kwargs["proxies"].upper():
                    proxies = None
                elif kwargs["proxies"].upper() != "YES" or kwargs["proxies"].upper() != "NOT":
                    proxies = json.loads(kwargs["proxies"])
            else:
                proxies = None
        except:
            proxies = None
        return proxies

    def post_response(self, method,_url, parameters=None, _headers=None, payload=None,verify=True, **kwargs):
        """
        Description: This method is used to receive the response from REST API Endpoint(POST)\n
        :param url: API url for POST request\n
        :param parameters: Input parameter or payload or Key value of API (if any)\n
        :param _headers: Headers if any\n
        :param payload: JSON Request Payload\n
        :param verify: set to True by default, used for secure https connection\n
        :param _username: User Authentication of API (if any)\n
        :param _password: ****** (if any/use the python password encryption method to get the encrypted password)\n
        :param proxies: proxies if applicable\n
        :return: response object\n

        Note: This Method only validate service not the service DATA **
        """
        _authentication = self.get_user_credentials(**kwargs)
        _proxies = self.get_proxies(**kwargs)

        if "files" in kwargs:
            _files = kwargs["files"]
        else:
            _files = None

        if not isinstance(payload, str):
            payload = json.dumps(payload)
        else:
            logger1.info("Payload Default as String..........")

        try:
            if method == 'POST':
                response1 = requests.post(url=_url, headers=_headers, params=parameters, data=payload,
                                          auth=_authentication, verify=verify, proxies=_proxies, files = _files)
            elif method == 'REST':
                response1 = requests.get(url=_url, headers=_headers, params=parameters, data=payload,
                                          auth=_authentication, verify=verify, proxies=_proxies, files=_files)
            logger1.info("successfuly connected to API..........")
        except Exception as Ex:
            response1 = False
            # print("Error connecting to API..........",EX+ str(Ex))
            logger1.info("Error connecting to API.........."+ str(Ex))
        return response1

    
