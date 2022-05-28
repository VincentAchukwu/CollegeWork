# general libraries needed
import pandas as pd, pandas_datareader as web, os, requests

# flask

from flask import Flask, render_template, request, redirect, Response, session

# Twitter-related, regular expression, and news api libraries
import tweepy, textblob, re
from newsapi import NewsApiClient

# ARIMA and figure canvas libraries
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

# matplotlib for plotting, and other plotting-related libraries
import matplotlib.pyplot as plt, io, base64
import statsmodels.api as sm
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO

# relativedelta for adding dates together
import datetime as dt, timeago
from dateutil.relativedelta import *

# dotenv for loading keys
from dotenv import load_dotenv
import mpld3

# loading the TIINGO API key for obtaining cryptocurrency prices
load_dotenv()
TIINGOKEY = os.getenv("TIINGOKEY")

# loading keys from Twitter API
APIKey = os.getenv("APIKey")
APIKeySecret = os.getenv("APIKeySecret")
BearerToken = os.getenv("BearerToken")
AccessToken = os.getenv("AccessToken")
AccessTokenSecret = os.getenv("AccessTokenSecret")

# authenticated to Twitter API
authenticator = tweepy.OAuthHandler(APIKey, APIKeySecret)
authenticator.set_access_token(AccessToken, AccessTokenSecret)

# initialising Twitter and News API
twitterAPI = tweepy.API(authenticator, wait_on_rate_limit=True)
newsAPI = NewsApiClient(api_key=os.getenv("NewsAPI"))

# flask session key for storing variables in sessions for the portfolio page
sessionKey = os.getenv("SessionKey")

# initialising Flask app
app = Flask(__name__)

# using top 20 cryptocurrencoes as the options users can select from in dropdown menu
# in the following pages: prediction, sentiment, and portfolio selectors
crypto = {
    "Bitcoin": "BTC",
    "Ethereum": "ETH",
    "BNB": "BNB",
    "XRP": "XRP",
    "Terra": "LUNA",
    "Cardano": "ADA",
    "Solana": "SOL",
    "Avalanche": "AVAX",
    "Polkadot": "DOT",
    "Dogecoin": "DOGE",
    "Shiba Inu": "SHIB",
    "Polygon": "MATIC",
    "Cosmos": "ATOM",
    "Litecoin": "LTC",
    "NEAR Protocol": "NEAR",
    "Chainlink": "LINK",
    "Uniswap": "UNI",
    "TRON": "TRX",
    "Bitcoin Cash": "BCH",
    "Stellar": "XLM"
}

# using a dictionary of filter options so that we can use alternate name for the api filters
# (e.g instead of the filter option showing "publishedAt", it can say "Latest", more readable)
filterOptions = {
    "Most Relevant": "relevancy",
    "Most Popular": "popularity",
    "Latest": "publishedAt"
}


# homepage route
@app.route("/")
def home():
    return render_template("home.html")


# selectPrediction route - where user will select a cryptocurrency to view predictions for
@app.route("/selectPrediction", methods=["GET", "POST"])
def selectPrediction():
    # using a dictionary then converting keys to list to avoid hardcoding later on
    cryptoCoins = list(crypto.keys())
    return render_template("coinForecastSelector.html", cryptoCoins=cryptoCoins)


# flask route for displaying the graph for the selected cryptocurrency
@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    # clearing the graph prior to showing the predictions for selected coin
    plt.clf()
    img = BytesIO()
    if request.method == "POST":
        # obtaining the selected coin from the dropdown
        coinName = request.form.get("selectedCoin")
        daysSelected = int(request.form.get("daysSelected"))
        # using dictionary to get the corresponding ticker (for readability on the graph e.g Bitcoin (BTC))

        coinTicker = crypto[coinName]
        # retrieving the dataset from TIINGO
        df = getCryptoData(coinTicker)
        # retrieving prediction via passing dataset to predict function
        prediction = predict(df, daysSelected)
        # obtaining the current price and the predicted price to determine buy/sell signal
        currentPrice = df.close[-1]
        predictedPrice = prediction.values[-1]
        percentageDifference = "{:.4f}".format((abs(currentPrice - predictedPrice) / currentPrice) * 100)
        df["Close First Difference"] = df["close"] - df["close"].shift(2)
        # configuring the plot via matplotlib for now (planning to upgrade to JavaScript chart)
        ax = df["close"].plot(color="blue", label="Close")
        preds = prediction.plot(ax=ax, color="red", label="Predicted Close").get_figure()
        plt.title("{} ({}-EUR) Prediction".format(coinName, coinTicker))
        plt.legend()
        fig = plt.figure(figsize=(12, 8))
        ax1 = fig.add_subplot(211)
        fig = sm.graphics.tsa.plot_acf(df["close"].iloc[2:], lags=40, ax=ax1)
        ax2 = fig.add_subplot(212)
        fig2 = sm.graphics.tsa.plot_pacf(df["Close First Difference"].iloc[2:], lags=40, ax=ax2).get_figure()
        plt.title("{} ({}-EUR) Close First Difference".format(coinName, coinTicker))

        buf = io.BytesIO()
        # saves photo to bytes
        preds.savefig(buf, format='png')
        buf.seek(0)
        buffer = b''.join(buf)
        # changes it to 64bit
        b2 = base64.b64encode(buffer)
        # allows it to be passed over to the front end using preds2
        preds2 = b2.decode('utf-8')
        # use of mpld3
        plt_html = mpld3.fig_to_html(preds)
        # same format as the first graph
        buf = io.BytesIO()
        fig2.savefig(buf, format='png')
        buf.seek(0)
        buffer = b''.join(buf)
        b2 = base64.b64encode(buffer)
        figs2 = b2.decode('utf-8')

        plt_html1 = mpld3.fig_to_html(fig2)

        # passing the plot to coinForecastGraph.html
        return render_template("coinForecastGraph.html", coinName=coinName, currentPrice=currentPrice,
                               predictedPrice=predictedPrice, percentageDifference=percentageDifference,
                               plt_html=plt_html, plt_html1=plt_html1, ax=ax, preds=preds2, fig2=figs2)


# helper function for getting historic price of selected cryptocurrency via TIINGO API
def getCryptoData(coinTicker):
    # setting default crypto-fiat currency pair to EUR
    againstCurrency = "EUR"

    # specifying an early start date for the selected coin so the API will retrieve the earliest start 
    # date available for historic prices if it doesn't match the specified start date
    start = dt.datetime(2015, 1, 1)
    # end date is the current date
    end = dt.datetime.now()

    data = web.get_data_tiingo("{}{}".format(coinTicker, againstCurrency), start, end, api_key=TIINGOKEY)
    # dropping any N/A values in case
    data = data.dropna()
    # removing multi-index via resetting the index to just the date column
    data = data.reset_index()
    data = data.set_index("date")

    return data


# helper function for obtaining the prediction for the selected coin
def predict(coinDataset, daysSelected):
    # running auto_arima on the selected coin closing price to get its best p, d, q values
    # predictions not looking so good long term, perhaps short term predictions would suit
    stepwise_fit = auto_arima(coinDataset["close"], trace=True, suppress_warnings=True, test="adf")
    order = stepwise_fit.get_params().get("order")

    # training the model now based on entire dataset to make future predictions
    model = ARIMA(coinDataset["close"], order=order)
    model = model.fit()
    # print(coinDataset.tail())  # checking what the last date is, then predict from this day onward

    # predicting from the current date onwards
    startDate = dt.datetime.now()

    # for testing, let's predict the x days into the future (depending on how many days user selected)
    indexFutureDates = pd.date_range(start=startDate.strftime("%Y-%m-%d"),
                                     end=(startDate + relativedelta(days=+daysSelected)).strftime("%Y-%m-%d"))
    prediction = model.predict(start=len(coinDataset), end=len(coinDataset) + daysSelected, typ="levels")
    # like before, we're handling dataset for indexing so we can plot it
    prediction.index = indexFutureDates
    # converting to pandas dataframe and creating columns (this MIGHT be needed for JavaScript chart)
    # predictionToDf = pd.DataFrame({"date": prediction.index, "predictedClose": prediction.values})
    # print(predictionToDf)

    return prediction


# similar to selectPrediction route, user will select a coin to view its market sentinemt from Twitter
@app.route("/selectSentiment")
def selectSentiment():
    cryptoCoins = list(crypto.keys())
    return render_template("coinSentimentSelector.html", cryptoCoins=cryptoCoins)

@app.route("/technicalAnalysis")
def technicalAnalysis():
    return render_template("technicalAnalysis.html")


# market sentiment displayed in this route
@app.route("/sentiment", methods=["GET", "POST"])
def sentiment():
    if request.method == "POST":
        # obtaining the selected coin from the dropdown
        coinName = request.form.get("selectedCoin")
        # using dictionary to get the corresponding ticker (for readability on the graph e.g Bitcoin (BTC))
        coinTicker = crypto[coinName]
        # passing the coin name to tweepy to obtain its market sentiment
        positive, negative, = getTweets(coinName)[0], getTweets(coinName)[1]
        neutral = abs(100 - (positive + negative))
        # passing the plot to coinSentimentGraph.html
        return render_template("coinSentimentGraph.html", coinName=coinName, coinTicker=coinTicker,
                               positive=positive, neutral=neutral, negative=negative)

    cryptoCoins = list(crypto.keys())
    return render_template("coinSentimentSelector.html", cryptoCoins=cryptoCoins)


# helper function for obtaining tweets
def getTweets(coin):
    # looking at ordinary tweets rather than retweets for now
    search = f"#{coin} -filter:retweets"
    # .items() used for specifying how many tweets we want to obtain
    tweetCursor = tweepy.Cursor(twitterAPI.search_tweets, q=search, lang="en", tweet_mode="extended").items(100)
    # list of tweets in text form
    tweets = [tweet.full_text for tweet in tweetCursor]

    # converting to dataframe
    tweets_df = pd.DataFrame(tweets, columns=["Tweets"])
    # cleaning the data (removing tags, hashtags, etc)
    for _, row in tweets_df.iterrows():
        row["Tweets"] = re.sub("http\S+", "", row["Tweets"])
        row["Tweets"] = re.sub("#\S+", "", row["Tweets"])
        row["Tweets"] = re.sub("@\S+", "", row["Tweets"])
        row["Tweets"] = re.sub("\\n", "", row["Tweets"])  # double backslash so it makes \n a null char

    # performing sentiment analysis per tweet and assigning their polarity score
    tweets_df["Polarity"] = tweets_df["Tweets"].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
    # if polarity is greater than 0, positive, else negative
    tweets_df["Result"] = tweets_df["Polarity"].map(lambda pol: "+" if pol > 0 else "-")

    # count all tweets where result is positive and negative
    positive = tweets_df[tweets_df.Result == "+"].count()["Tweets"]
    negative = tweets_df[tweets_df.Result == "-"].count()["Tweets"]

    # returning the positive & negative market sentiment via list so we can read it from sentiment()
    return [positive, negative]


# route to search results page
@app.route("/searchResults", methods=["GET", "POST"])
def results():
    # if user makes a POST request
    if request.method == "POST":
        # access data inside
        query = request.form.get("query")
        selectedFilter = request.form.get("selectedFilter")
        # if the query is not empty, pass it to the news api
        if query:
            # save the current query to a global variable if the user wants to later apply a filter on the same query
            global cachedQuery
            cachedQuery = query

            # by default, sorting by relevancy (if param not specified, newsapi sorts by recency by default)
            response = newsAPI.get_everything(
                q=query,
                language="en",
                sort_by="relevancy",
                page_size=100
            )

            # formatting the date to timeAgo format
            refactoredResponse = publishedDateFormatter(response)

            # bring them to results.html displaying query results
            return render_template("results.html",
                                   response=response["articles"],
                                   query=query,
                                   filterOptions=list(filterOptions.keys())
                                   )

        # else if the query was entered but a filter was applied
        elif query is None:

            # restore the original query and apply the filter to it
            query = cachedQuery

            # reordering the temp list of filters so the selected filter will be displayed first on the dropdown (so the user will 
            # know which filter they selected)
            selectedFilterValue = filterOptions[selectedFilter]
            filterOptionsReordered = list(filterOptions.keys())
            filterOptionsReordered.remove(selectedFilter)
            filterOptionsReordered.insert(0, selectedFilter)

            # sorting by the filter that the user selected
            response = newsAPI.get_everything(
                q=cachedQuery,
                language="en",
                sort_by=selectedFilterValue,
                page_size=100
            )

            # formatting the date to timeAgo format
            refactoredResponse = publishedDateFormatter(response)

            # bring them to results.html displaying query results
            return render_template("results.html",
                                   response=response["articles"],
                                   query=query,
                                   selectedFilter=selectedFilter,
                                   filterOptions=filterOptionsReordered
                                   )

        # else the query is empty, (newsapi raises exception if empty query is passed as input)
        return render_template("results.html", query=query)


# helper function for results() to reformat the date/time entry of when article was published
def publishedDateFormatter(response):
    # obtain current date for timeAgo functionality (for comparing current date with article publish date)
    now = dt.datetime.now()
    date_format = "%Y-%m-%dT%H:%M:%SZ"

    # changing the "publishedAt" date to a timeAgo format
    # (e.g instead of showing a date, it'll show something like "x hours ago", etc)
    for result in response["articles"]:
        publishedDate = dt.datetime.strptime(result["publishedAt"], date_format)
        timeAgoFormat = timeago.format(publishedDate, now)
        result["publishedAt"] = timeAgoFormat

    return response


# fng = Fear And Greed
# obtaining fear and greed for current date, previous day, previous week, and previous month
@app.route("/fng")
def fearAndGreed():
    # first tile (in fearAndGreed.html) showing fng of today via graph by passing current date to API to
    # obtain the image graph
    currDate = dt.datetime.now()
    # Replace "-" with "#" if using Windows (see here: https://www.kite.com/python/answers/how-to-remove-leading-0's-in-a-date-in-python)
    # if using windows:
    # currDateString = currDate.strftime("%Y-%#m-%#d")
    # if using linux
    currDateString = currDate.strftime("%Y-%-m-%-d")

    currDateURL = "https://alternative.me/images/fng/crypto-fear-and-greed-index-{}.png".format(currDateString)

    # now we're storing the historic fng values (including todays) for the second tile
    historicValues = {}
    # limit=32 because we want to see fng over the last month
    fngIndexes = requests.get("https://api.alternative.me/fng/?limit=32")
    fngIndexesJson = fngIndexes.json()["data"]

    # obtaining historic fng values and their corresponding classification
    # (format of dictionary) historicValues{"timeOfMonth": [fng value, fng meaning]}
    historicValues["Today"] = [int(fngIndexesJson[0]["value"]), fngIndexesJson[0]["value_classification"]]
    historicValues["Yesterday"] = [int(fngIndexesJson[1]["value"]), fngIndexesJson[1]["value_classification"]]
    historicValues["Last Week"] = [int(fngIndexesJson[7]["value"]), fngIndexesJson[7]["value_classification"]]
    historicValues["Last Month"] = [int(fngIndexesJson[30]["value"]), fngIndexesJson[30]["value_classification"]]

    # converting timestamp to int for frontend to convert the time left in seconds into hours, minutes, and secs
    secondsUntilUpdate = int(fngIndexesJson[0]["time_until_update"])

    # passing generated fng images to html page to display it
    return render_template("fearAndGreed.html", todaysGraph=currDateURL, historicValues=historicValues,
                           secondsLeft=secondsUntilUpdate)


# idea: have a separate route that basically determines whether to go to the selector or the summary itself
# on first access, you select coins, but when you press "edit portfolio", THAT'S when you can edit the portfolio
@app.route("/portfolio")
def portfolio():
    # if user wants to visit portfolio given that they already selected the coins initially, display it
    if session.get("selectedCoinsList"):
        oldSelectedCoinsList = session.get("selectedCoinsList")
        tradingViewSymbols = [["BINANCE:{}EUR".format(crypto[coin])] for coin in oldSelectedCoinsList]
        return render_template("portfolioSummary.html", tradingViewSymbols=tradingViewSymbols)

    # else, let them edit portfolio/create a new one if visiting site on a new session
    # (in the URL, it'll still say "/portfolio" instead of "/portfolioSelector" since we're 
    # calling a function from "/portfolio" (unless we click on the "edit portfolio" button))
    return portfolioSelector()


# user selects coins to add to portfolio summary
@app.route("/portfolioSelector")
def portfolioSelector():
    cryptoCoins = list(crypto.keys())
    return render_template("portfolioSelector.html", cryptoCoins=cryptoCoins)


# display statistical summary based on the user-selected coins
@app.route("/portfolioSummary", methods=["GET", "POST"])
def portfolioSummary():
    # if user makes a POST request
    if request.method == "POST":
        # obtaining list of user-selected coins
        selectedCoinsList = request.form.getlist("selectedCoins")
        # save the user-selected coins in current session so user can avoid having to re-add coins to 
        # current portfolio per session
        session["selectedCoinsList"] = selectedCoinsList
        # then converting list to the following format: "BINANCE:BTCEUR" (for tradingView chart JS)
        tradingViewSymbols = [["BINANCE:{}EUR".format(crypto[coin])] for coin in selectedCoinsList]

    # passing selected coins as well as all the top 20 coins (for mapping selected coin with ticker for the graph)
    return render_template("portfolioSummary.html", tradingViewSymbols=tradingViewSymbols)


# for now, enable debugging mode
if __name__ == "__main__":
    # app session requires a key
    app.secret_key = sessionKey
    app.run(debug=True, host="0.0.0.0", port=5000)
