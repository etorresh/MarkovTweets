from time import sleep
from datetime import datetime
import threading
import random
import logging
import os

from . import markov_chain
from . import string_control


class MarkovTweets:
    def __init__(self, api, settings):
        self.api = api
        self.settings = settings
        self.chain = markov_chain.build_chain(markov_chain.read_file(settings["markov_chain_source"]))

    def automatic_sentence(self):
        while True:
            if self.settings["random_hashtag"]:
                if random.random() <= self.settings["random_hashtag_percentage"]:
                    hashtag = random.choice(self.api.trending_type("116545", "Hashtag"))
                else:
                    hashtag = ""

            random_message = markov_chain.create_message(self.chain, max_length=self.settings["tweet_max_words"])
            random_message = string_control.clean_blank_space(random_message)
            random_message = string_control.limit_check(random_message, self.settings["twitter_char_limit"], hashtag)
            self.api.update_status(random_message)

            sleep(self.settings["random_message_timer"])

    def start(self):
        if self.settings["random_message"]:
            threading.Thread(target=self.automatic_sentence).start()

        if os.path.exists("last_tweet_id.txt"):
            with open('last_tweet_id.txt', 'r+') as file:
                old_tweet_id = file.read().replace('\n', '')
        else:
            open('last_tweet_id.txt', 'w').close()
            old_tweet_id = None

        while True:
            r = self.api.get_mentions()
            if r.status_code == 429:
                logging.warning("API limit reached." + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            elif str(r.json()[0]["id"]) != old_tweet_id:
                for response in r.json():
                    if old_tweet_id != str(response["id"]):
                        input_starting_sentence = response["text"].replace(self.settings["bot_username"], "")
                        message = markov_chain.create_message(self.chain, max_length=self.settings["tweet_max_words"], starting_sentence=input_starting_sentence)
                        final_message = string_control.clean_blank_space(message)
                        final_message = string_control.limit_check(final_message, self.settings["twitter_char_limit"], " @" + response["user"]["screen_name"])
                        self.api.update_status(final_message, in_reply_to_status_id=response["id"])
                    else:
                        break

                old_tweet_id = str(r.json()[0]["id"])
                with open('last_tweet_id.txt', 'w') as file:
                    file.write(old_tweet_id)
            sleep(12)
