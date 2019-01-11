# Main pipeline for Twitter Markov bot.
# Made by MadreNodriza. https://github.com/MadreNodriza


import markov_chain
import string_control
import requests
from requests_oauthlib import OAuth1
import tweepy
import time

# Twitter API data
api_public = ""
api_private = ""
token_public = ""
token_private = ""

#Settings
bot_username = ""
extra_message = ""
api_delay = 10
training_data = "example_source.txt"

t_auth = tweepy.OAuthHandler(api_public, api_private)
t_auth.set_access_token(token_public, token_private)

api = tweepy.API(t_auth)

mentions_url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"
auth = OAuth1(api_public, api_private, token_public, token_private)

chain = markov_chain.build_chain(markov_chain.read_file(training_data))

with open('latest_tweet.txt', 'r') as file:
		old_response = file.read().replace('\n', '')
while(True):
	response = requests.get(mentions_url, auth=auth)
	if(response.status_code == 429):
		print("Warning: API limit reached.")
	elif(response.json()[0]["text"] != old_response):
		print("Warning: new Tweet detected. ")
		old_response = response.json()[0]["text"]
		with open('latest_tweet.txt', 'w') as file:
			file.write(old_response)
		input_starting_sentence = response.json()[0]["text"].replace(bot_username, "")
		tweet_id = response.json()[0]["id"]
		user = "@" + response.json()[0]["user"]["screen_name"]
		
		message = markov_chain.create_message(chain, starting_sentence = input_starting_sentence)
		clean_message = string_control.super_detox(message)
		final_message = clean_message + " " + user + " " + extra_message
		api.update_status(final_message, in_reply_to_status_id = tweet_id)
	else:
		print("Warning: no new tweets detected. ")
	time.sleep(api_delay)

