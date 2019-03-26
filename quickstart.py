import twitter_handler
import markovtweets

# API credentials
api_public = ""
api_private = ""
token_public = ""
token_private = ""
bot_username = ""

# Settings
settings = {
    "markov_chain_source": "example_source.txt",
    "tweet_max_words": 25,
    "twitter_char_limit": 280,
    "random_message": True,
    "random_message_timer": 12 * 60 * 60
}

api = twitter_handler.TwitterHandler(api_public, api_private, token_public, token_private)
MT = markovtweets.MarkovTweets(api, settings)
MT.start()
