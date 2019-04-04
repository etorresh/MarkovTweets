import requests
from requests_oauthlib import OAuth1
import logging

base_url = "https://api.twitter.com/"
status_url = "{}1.1/statuses/update.json".format(base_url)
trending_url = "{}1.1/trends/place.json?id=".format(base_url)
mentions_url = "{}1.1/statuses/mentions_timeline.json".format(base_url)


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

    def trending(self, geo_id, amount_of_trends=50):
        geo_url = trending_url + geo_id
        trends = requests.get(geo_url, auth=self.auth)
        trends_list = []
        for y in range(amount_of_trends):
            trends_list.append((trends.json()[0]["trends"][y]["name"]))
        return trends_list

    # 0 = Topic, 1 = Hashtag
    def trending_type(self, geo_id, topic_or_hashtag, amount_of_trends=50):
        if topic_or_hashtag == "Topic":
            topic_or_hashtag = 0
        elif topic_or_hashtag == "Hashtag":
            topic_or_hashtag = 1
        else:
            logging.error("Set topic_or_hashtag to 'Topic' or 'Hashtag' to search for an specific trend type.")
        trends = self.trending(geo_id, amount_of_trends)
        trending_list = []
        for trend in trends:
            if trend.__contains__("#") == topic_or_hashtag:
                trending_list.append(trend)
        return trending_list

    def get_mentions(self):
        return requests.get(mentions_url, auth=self.auth)
