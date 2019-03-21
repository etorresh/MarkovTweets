import requests
from requests_oauthlib import OAuth1

base_url = "https://api.twitter.com/"
status_url = "{}1.1/statuses/update.json".format(base_url)


class TwitterHandler:

    def __init__(self, api_public, api_private, token_public, token_private):
        self.api_public = api_public
        self.api_private = api_private
        self.token_public = token_public
        self.token_private = token_private
        self.auth = OAuth1(api_public, api_private, token_public, token_private)

    def update_status(self, text_of_the_status, in_reply_to_status_id=""):
        status_params = {
            "status": text_of_the_status,
            "in_reply_to_status_id": in_reply_to_status_id
        }

        return requests.post(status_url, auth=self.auth, params=status_params).status_code
