<p align="center">
  <a href="https://en.wikipedia.org/wiki/Andrey_Markov">
  <img src="https://i.imgur.com/S9I6xnN.png" width="300">
  </a>
  <h1 align="center">MarkovTweets</h1>
  <p align="center">A Python twitter bot that uses a markov chain based sentence generator to fill in tweets.<p>
  <p align="center">
      <a href="https://github.com/madrenodriza/MarkovTweets/blob/master/LICENSE.txt"/>
      <img src="https://img.shields.io/github/license/madrenodriza/markovtweets.svg" />
    </a>
      <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
  
## DEPRECATED: No longer maintained.
## Feature list:
  - **Tag reply:** replies to tweets that mention the bot.
  
  - **Automatic tweets:** randomly tweets sentences. Time interval can be adjusted at settings.
  
  - **Current trends:** trending hashtags can be added to tweets. The probability of using a hashtag can be adjusted at settings.
  
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
