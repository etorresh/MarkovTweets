<p align="center">
  <img src="https://imgur.com/download/aFYrBn7" width="300">
  </p>
  
# MarkovTweets
## Description:
  A Python twitter bot that uses a markov chain based sentence generator to fill in tweets.
  
## Feature list:
  - **Tag reply:** replies to tweets that mention the bot.
  
  - **Automatic tweets:** randomly tweets sentences. Time interval can be adjusted at settings.
  
  - **Current trends:** trending hashtags can be added to automatic tweets. The probability of using a hashtag can be adjusted at settings.
  
## Installation:
```
pip install MarkovTweets
```
**That's it! ✈**

Download the **[quickstart](https://cdn.jsdelivr.net/gh/madrenodriza/markovtweets/example/quickstart.py)** script to your machine.

You can put your app account details by passing the API credential, like so:
```
api_public = "API_KEY"
api_private = "API_SECRET_KEY"
token_public = "ACCESS_TOKEN"
token_private = "ACESS_TOKEN_SECRET"
```

Set your bot username the same as your twitter username and reference the markov chain source. Here's a **[markov chain source example](https://github.com/madrenodriza/MarkovTweets/blob/master/example/example_source.txt)**.
```
settings = {
    "markov_chain_source": "example_source.txt",
    "bot_username": "TWITTER_USERNAME",
}
```
To run MarkovTweets, you'll need to run the **[quickstart](https://cdn.jsdelivr.net/gh/madrenodriza/markovtweets/example/quickstart.py)** script you've just downloaded.
```
python quickstart.py
```
  
## Example project:
[Amlo Simulador](http://www.twitter.com/AmloSimulador)
