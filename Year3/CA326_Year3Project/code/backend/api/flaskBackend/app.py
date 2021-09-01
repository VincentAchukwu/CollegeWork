# Flask Backend API

from flask import Flask, request
from flask_cors import CORS

import requests

app = Flask(__name__)
CORS(app)

# route to view conversion of fromCurrency to toCurrency with given amount
@app.route("/api/conversions")
def convert():

    # obtaining input from frontend via URL parameters
    fromCurrency = request.args.get("fromCurr").upper()
    toCurrency = request.args.get("toCurr").upper()
    amount = request.args.get("amount")

    # if the currency codes and amount are valid, proceed
    try:
        from rates import rates
        assert((fromCurrency in rates) and (toCurrency in rates)) == True
        # check if it's a number, and bigger than 0
        assert(amount.replace('.','',1).isdigit())
        # if so, convert to float
        amount = float(amount)
        assert( amount > 0 ) == True
    # else, raise an error and inform user in frontend
    except AssertionError:
        # returning "flag" for frontend to know to display error message
        return {"requestedConversion": [
            {"key": "invalid"}
            ]}

    # passing inputs to api endpoint url
    conversionEndpoint = "https://data.fixer.io/api/convert?access_key=c25d971c381d704fcdf03554750dddf2&from={}&to={}&amount={}".format(
        fromCurrency, toCurrency, amount
    )

    # gets response from Fixer API conversion endpoint
    response = requests.get(conversionEndpoint)
    responseJson = response.json()

    # rounding to 2 d.p
    result = "{:05.2f}".format(responseJson["result"])

    conversionInfo = [
        {"key": result}
    ]

    return {"requestedConversion": conversionInfo}

# helper function for getRates
def ratesResponse(url):

    # storing list of dictionaries from fixer API response
    rates = []

    # gets response from Fixer API rates endpoint
    response = requests.get(url)
    responseJson = response.json()

    # retrieving the rates output from the response
    dictRates = responseJson["rates"].items()

    # iterating through the dict response and 
    # adding the currency and their corresponding rates
    for currency, rate in dictRates:
        rates.append({"key": currency, "rate": "{:05.2f}".format(rate)})

    return rates

# route to view requested rates
@app.route("/api/rates")
def getRates():

    # getting input from url parameters
    baseCurr = request.args.get("base").upper()
    date = request.args.get("date").upper()
    currencyCodes = request.args.get("rates").upper()
    # used for adding each input to JSON
    symbols = ",".join(currencyCodes.split())

    # if base currency specified, check if it's valid
    if len(baseCurr) > 0:
        try:
            from rates import rates
            assert(baseCurr in rates)
        except AssertionError:
            return {"requestedRates": [
                {"key": "invalid"}
                ]}

    # Historical rates available up to 1999 on Fixer API
    # checking here that the date isn't before that (if specified)
    if len(date) > 0:
        try:
            from datetime import datetime
            # compare date input to current date (can't get rate from the future..)
            currDate = datetime.today().strftime("%Y-%m-%d")
            assert("1999-1-01" <= date <= currDate)
            # easy way of dealing with zero padding, make sure length is valid
            assert(len(date) == 10)
            # makes sure dates are valid format (e.g not 2020-69-42)
            assert datetime.strptime(date, "%Y-%m-%d")
        # if date invalid
        except (AssertionError, ValueError):
            # returning "flag" for frontend to know to display error message
            return {"requestedRates": [
                {"key": "invalid"}
                ]}

    # if the currency codes are valid, proceed
    try:
        from rates import rates
        currencies = currencyCodes.split()
        for code in currencies:
            assert(code in rates)
    # else, raise an error and inform user in frontend
    except AssertionError:
        # returning "flag" for frontend to know to display error message
        return {"requestedRates": [
            {"key": "invalid"}
            ]}

    # if user wants certain currency rates 
    # & base currency & date not specified
    # (base currency default is EUR)
    if (len(baseCurr) == 0) and (len(date) == 0):

        latestRates = "https://data.fixer.io/api/latest?access_key=c25d971c381d704fcdf03554750dddf2&symbols={}&format=1".format(
            symbols
        )
        rates = ratesResponse(latestRates)

    # else if user wants certain rates & date specified
    # & base currency not specified
    elif (len(baseCurr) == 0):

        latestRates = "https://data.fixer.io/api/{}?access_key=c25d971c381d704fcdf03554750dddf2&symbols={}&format=1".format(
            date, symbols
        )
        rates = ratesResponse(latestRates)
    
    # else if user wants certain rates & base currency specified
    # & date not specified
    elif (len(date) == 0):
        latestRates = "https://data.fixer.io/api/latest?access_key=c25d971c381d704fcdf03554750dddf2&symbols={}&base={}&format=1".format(
            symbols, baseCurr
        )
        rates = ratesResponse(latestRates)

    # else user wants certain rates, date, and base currency
    else:
        latestRates = "https://data.fixer.io/api/{}?access_key=c25d971c381d704fcdf03554750dddf2&symbols={}&base={}&format=1".format(
            date, symbols, baseCurr
        )
        rates = ratesResponse(latestRates)

    requestedRates = {"requestedRates": rates}

    # frontend receives result
    return requestedRates

# route to retrieve exchange rates of currencies given date range
@app.route("/api/timeSeries")
def currencyTimeSeries():

    # importing datetime for handling 6-month time range
    from datetime import datetime, timedelta
    from dateutil.relativedelta import relativedelta
    import requests

    # # obtaining input from frontend via URL parameters
    fromCurrency = request.args.get("fromCurr").upper()
    toCurrency = request.args.get("toCurr").upper()

    # if the currency codes are valid, proceed
    try:
        from rates import rates
        assert((fromCurrency in rates) and (toCurrency in rates)) == True

    # else, raise an error and inform user in frontend
    except AssertionError:
        # returning "flag" for frontend to know to display error message
        return {"requestedTimeSeries": [
            {"key": "invalid"}
            ]}

    # current date aka end_date (since we're going with the trend of last 6 months)
    currDateObject = datetime.today()
    # aka start_date (6 months from current date)
    startDateObject = (currDateObject - relativedelta(weeks=6))
    startDate = startDateObject.strftime("%Y-%m-%d")
    # stringifying currDateObject to YYY-MM-DD format
    currDate = currDateObject.strftime("%Y-%m-%d")

    # initialising JSON structure for frontend
    currencyTimeRange = {"requestedTimeSeries": []}

    # the end date is the current date,
    # base currency is the currency we're converting from
    # symbols is the currency we want results for
    timeSeriesRates = "https://data.fixer.io/api/timeseries?access_key=c25d971c381d704fcdf03554750dddf2&start_date={}&end_date={}&base={}&symbols={}&format=1".format(
        startDate, currDate, fromCurrency, toCurrency
    )

    # gets response from Fixer API timeseries endpoint
    response = requests.get(timeSeriesRates)
    responseJson = response.json()

    dictRates = responseJson["rates"].items()

    # daySkipper used for iterating every 5 days through the Fixer JSON data
    daySkipper = 1
    # iterating over dates
    for date, rates in dictRates:
        if ((currDateObject - datetime.strptime(date, "%Y-%m-%d")).days % 7 == 0) and (daySkipper <= 7):
            # for the current date, retrieve currency rate(s)
            # for currency, rate in rates.items():
                # day within the last 6 months
            result = "{:05.2f}".format(rates[toCurrency])
            currencyTimeRange["requestedTimeSeries"].append({"key": date, "code": toCurrency, "rate": result})
            daySkipper += 1

    # deleting first date to make it 6 instead of 7 dates for the graph
    del currencyTimeRange["requestedTimeSeries"][0]

    return currencyTimeRange


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
