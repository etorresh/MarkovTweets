# local libs
import markov_chain
import string_control
import twitter_handler

# general libs
from time import sleep
from datetime import datetime
import threading

# API credentials
api_public = ""
api_private = ""
token_public = ""
token_private = ""
bot_username = ""

# Settings
markov_chain_source = "example_source.txt"
tweet_max_words = 25
random_message_timer = 12 * 60 * 60
twitter_char_limit = 280

api = twitter_handler.TwitterHandler(api_public, api_private, token_public, token_private)

chain = markov_chain.build_chain(markov_chain.read_file(markov_chain_source))

with open('last_tweet_id.txt', 'r') as file:
    old_tweet_id = file.read().replace('\n', '')


def automatic_sentence():
    while True:
        random_message = markov_chain.create_message(chain, max_length=tweet_max_words)
        random_message = string_control.clean_blank_space(random_message)
        random_message = string_control.limit_check(random_message, twitter_char_limit)
        api.update_status(random_message)

        sleep(random_message_timer)


threading.Thread(target=automatic_sentence).start()


while True:
    r = api.get_mentions()
    if r.status_code == 429:
        print("Warning: API limit reached." + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elif str(r.json()[0]["id"]) !=  old_tweet_id:
        print("Warning: new Tweet(s) detected. " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for response in r.json():
            if old_tweet_id != str(response["id"]):
                input_starting_sentence = response["text"].replace(bot_username, "")
                message = markov_chain.create_message(chain, max_length=tweet_max_words, starting_sentence=input_starting_sentence)
                final_message = string_control.clean_blank_space(message)
                final_message = string_control.limit_check(final_message, twitter_char_limit, " @" + response["user"]["screen_name"])
                api.update_status(final_message, in_reply_to_status_id=response["id"])
            else:
                break

        old_tweet_id = str(r.json()[0]["id"])
        with open('last_tweet_id.txt', 'w') as file:
            file.write(old_tweet_id)

    else:
        print("Warning: no new tweets detected. " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sleep(12)
