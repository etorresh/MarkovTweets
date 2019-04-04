from MarkovTweets import twitter_handler
from MarkovTweets import markovtweets

# api credentials
api_public = ""
api_private = ""
token_public = ""
token_private = ""

# Settings
settings = {
    "markov_chain_source": "example_source.txt",
    "bot_username": "",
    "tweet_max_words": 40,
    "twitter_char_limit": 280,
    "random_message": True,
    "random_message_timer": 12 * 60 * 60,
    "random_hashtag": True,
    "random_hashtag_percentage": 0.125
}

api = twitter_handler.TwitterHandler(api_public, api_private, token_public, token_private)
MT = markovtweets.MarkovTweets(api, settings)
MT.start()
