# Main pipeline for Twitter Markov bot.
# Made by MadreNodriza. https://github.com/MadreNodriza


import markov_chain
import string_control
import requests
from requests_oauthlib import OAuth1
import json
import tweepy
import time
import datetime

# API credentials
api_public = ""
api_private = ""
token_public = ""
token_private = ""

# Settings
bot_username = ""
tweet_max_length = 40


t_auth = tweepy.OAuthHandler(api_public, api_private)
t_auth.set_access_token(token_public, token_private)
api = tweepy.API(t_auth)

mentions_url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"
auth = OAuth1(api_public, api_private, token_public, token_private)

chain = markov_chain.build_chain(markov_chain.read_file("source.txt"))

with open('latest_tweet.txt', 'r') as file:
		 old_tweet_id = file.read().replace('\n', '')

while(True):
	r = requests.get(mentions_url, auth=auth)
	if(r.status_code == 429):
		print("Warning: API limit reached." + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	elif(str(r.json()[0]["id"]) !=  old_tweet_id):
		print("Warning: new Tweet(s) detected. " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		for response in r.json():
			if(old_tweet_id != str(response["id"])):
				input_starting_sentence = response["text"].replace(bot_username, "")
				message = markov_chain.create_message(chain, max = tweet_max_length, starting_sentence = input_starting_sentence)
				clean_message = string_control.super_detox(message)
				final_message = clean_message
				api.update_status(final_message, in_reply_to_status_id = response["id"])
			else:
				break
			
		old_tweet_id = str(r.json()[0]["id"])
		with open('latest_tweet.txt', 'w') as file:
			file.write(old_tweet_id)
		
	else:
		print("Warning: no new tweets detected. " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	time.sleep(30)