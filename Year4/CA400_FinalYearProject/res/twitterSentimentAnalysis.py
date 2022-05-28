# my twitter dev: https://developer.twitter.com/en/portal/products/elevated

import matplotlib.pyplot as plt
import os
import pandas as pd
import re
import textblob
import tweepy
from dotenv import load_dotenv

# obtaining the Twitter API keys from the .env file
load_dotenv()
APIKey = os.getenv("APIKey")
APIKeySecret = os.getenv("APIKeySecret")
BearerToken = os.getenv("BearerToken")
AccessToken = os.getenv("AccessToken")
AccessTokenSecret = os.getenv("AccessTokenSecret")

# authenticated to Twitter API
authenticator = tweepy.OAuthHandler(APIKey, APIKeySecret)
authenticator.set_access_token(AccessToken, AccessTokenSecret)

# initialising API, specifying topic as Bitcoin (or maybe a list of cryptocurrencies)
api = tweepy.API(authenticator, wait_on_rate_limit=True)
crypto = ["Bitcoin", "Ethereum", "Solana", "Cardano", "XRP"]

# specifying date range for the tweets (7-day limit) - idea: have date range within the last 7 days
# not sure if we need old tweets, might be better to have the latest tweets (current date)
# start = "2022-01-05"
# end = "2022-01-06"

def getTweets(crypto):

    # looking at ordinary tweets rather than retweets for now
    search = f"#{crypto} -filter:retweets"
    # .items() used for specifying how many tweets we want to obtain
    tweetCursor = tweepy.Cursor(api.search_tweets, q=search, lang="en", tweet_mode="extended").items(200)
    # list of tweets in text form
    tweets = [tweet.full_text for tweet in tweetCursor]


    # converting to dataframe
    tweets_df = pd.DataFrame(tweets, columns=["Tweets"])
    # cleaning the data (removing tags, hashtags, etc)
    for _, row in tweets_df.iterrows():
        row["Tweets"] = re.sub("http\S+", "", row["Tweets"])
        row["Tweets"] = re.sub("#\S+", "", row["Tweets"])
        row["Tweets"] = re.sub("@\S+", "", row["Tweets"])
        row["Tweets"] = re.sub("\\n", "", row["Tweets"])    # double backslash so it makes \n a null char

    # performing sentiment analysis per tweet and assigning their polarity score
    tweets_df["Polarity"] = tweets_df["Tweets"].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
    # if polarity is greater than 0, positive, else negative
    #tweets_df["Result"] = tweets_df["Polarity"].map(lambda pol: "+" if pol > 0 else "-")
    # if we're gonna include neutral, uncomment & replace
    tweets_df["Result"] = tweets_df["Polarity"].map(lambda pol: "+" if pol > 0 else ("=" if pol == 0  else "-"))

    # count all tweets where result is positive and negative
    positive = tweets_df[tweets_df.Result == "+"].count()["Tweets"]
    neutral = tweets_df[tweets_df.Result == "="].count()["Tweets"]  # if we're gonna include neutral, uncomment & replace
    negative = tweets_df[tweets_df.Result == "-"].count()["Tweets"]



    # plotting the data
   # plt.bar([0, 1], [positive, negative], label=["Positive", "Negative"], color=["green", "red"])
    # if we're gonna include neutral, uncomment & replace
    plt.bar([0, 1, 2], [positive, neutral, negative], label=["Positive", "Neutral", "Negative"], color=["green", "yellow", "red"])
    plt.title(crypto)
    plt.legend()
    plt.show()



for coin in crypto:
    getTweets(coin)
