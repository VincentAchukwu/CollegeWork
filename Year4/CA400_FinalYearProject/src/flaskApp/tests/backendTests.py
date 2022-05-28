# testing backend flask routes

import unittest, sys

# appending path so that we can import app.py which is one directory above this current one
sys.path.append("../")
from app import app


class TestFlaskApp(unittest.TestCase):

    # initialising app client so we can call it to get responses
    def setUp(self):
        # setting a mock secret key for unit testing since flask app requires session key
        app.config["SECRET_KEY"] = "mock_key"
        self.app = app.test_client()

    # testing navbar contents (since navbar contents are the same for each page, these unit tests are applied to each page to 
    # ensure that the navbar displays its contents as expected)
    def test_navbar(self):
        response1 = self.app.get("/")
        response2 = self.app.get("/selectPrediction")
        response3 = self.app.get("/selectSentiment")
        response4 = self.app.get("/fng")
        response5 = self.app.get("/portfolioSelector")
        response6 = self.app.get("/technicalAnalysis")

        # storing each response in a list and iterating over the list to apply the same test to each response
        responses = [response1, response2, response3, response4, response5, response6]

        # iterating over each response and apply the same tests to each (rather than having repetition of code)
        for response in responses:
            # testing if navbar contents are there (should pass for all pages)
            assert b"CoinCast" in response.data
            assert b"Home" in response.data
            assert b"Coin Forecast" in response.data
            assert b"Market Sentiment" in response.data
            assert b"Crypto Tools" in response.data
            assert b"Fear & Greed Index" in response.data
            assert b"Portfolio" in response.data
            assert b"Search for crypto news..." in response.data
            assert b"Technical Analysis" in response.data

            # testing response status
            self.assertEqual(response.status, "200 OK")
            self.assertNotEqual(response.status, "100 Multiple Choice")
            self.assertNotEqual(response.status, "300 Multiple Choice")
            self.assertNotEqual(response.status, "400 Bad Request")
            self.assertNotEqual(response.status, "404 Not Found")
            self.assertNotEqual(response.status, "500 Internal Server Error")

    # the tests below each have slightly similar but rather unique tests for each route

    # testing home route
    def test_home(self):

        # obtaining response from home page route
        response = self.app.get("/")

        # ensuring the header corresponds to the page we're on and that the wrong header is not displayed
        # (e.g if user in the home page, the page header should say "Home Page" and not "Portfolio Summary")
        assert b"Home Page" in response.data
        assert b"Coin Forecaster" not in response.data
        assert b"Coin Twitter Sentiment" not in response.data
        assert b"Crypto Fear and Greed" not in response.data
        assert b"Portfolio Selector" not in response.data
        assert b"Portfolio Summary" not in response.data
        assert b"Technical Analysis" not in response.data

    # testing prediction selection route
    def test_prediction_selector(self):

        # obtaining response from prediction selection route
        response = self.app.get("/selectPrediction")

        assert b"Coin Forecaster" in response.data
        assert b"Home Page" not in response.data
        assert b"Coin Twitter Sentiment" not in response.data
        assert b"Crypto Fear and Greed" not in response.data
        assert b"Portfolio Selector" not in response.data
        assert b"Portfolio Summary" not in response.data
        assert b"Technical Analysis" not in response.data

    # testing Sentiment selection route
    def test_sentiment_selector(self):

        # obtaining response from Sentiment selection route
        response = self.app.get("/selectSentiment")

        assert b"Coin Twitter Sentiment" in response.data
        assert b"Home Page" not in response.data
        assert b"Coin Forecaster" not in response.data
        assert b"Crypto Fear and Greed" not in response.data
        assert b"Portfolio Selector" not in response.data
        assert b"Portfolio Summary" not in response.data
        assert b"Technical Analysis" not in response.data

    # rate limit constantly being reached and it fails to obtain the tweets. might just leave it commented out just to show the
    # idea of how we'd test this route of the app
    # testing twitter sentiment summary route
    # def test_sentiment_summary(self):

    #     # obtaining responses from sentiment summary route via posting fake/mock "user selected" coins to sentiment page
    #     # then converting each response in text format to test contents of web page
    #     response1 = self.app.post("/sentiment", data={"selectedCoin": "Bitcoin"})
    #     response1Text = response1.get_data(as_text=True)

    #     response2 = self.app.post("/sentiment", data={"selectedCoin": "Ethereum"})
    #     response2Text = response2.get_data(as_text=True)

    #     response3 = self.app.post("/sentiment", data={"selectedCoin": "Polkadot"})
    #     response3Text = response3.get_data(as_text=True)

    #     response4 = self.app.post("/sentiment", data={"selectedCoin": "Terra"})
    #     response4Text = response4.get_data(as_text=True)

    #     response5 = self.app.post("/sentiment", data={"selectedCoin": "Chainlink"})
    #     response5Text = response5.get_data(as_text=True)

    #     response6 = self.app.post("/sentiment", data={"selectedCoin": "Stellar"})
    #     response6Text = response6.get_data(as_text=True)

    #     response7 = self.app.post("/sentiment", data={"selectedCoin": "Solana"})
    #     response7Text = response7.get_data(as_text=True)

    #     # storing all reponses in a dictionary embedded in a list
    #     responses = {
    #         "response1": [response1, response1Text],
    #         "response2": [response2, response2Text],
    #         "response3": [response3, response3Text],
    #         "response4": [response4, response4Text],
    #         "response5": [response5, response5Text],
    #         "response6": [response6, response6Text],
    #         "response7": [response7, response7Text]
    #     }

    #     print(responses["response1"][0])
    #     # iterating over each response to apply the same tests to each
    #     for response in responses.values():
    #         # response itself
    #         r = response[0]
    #         # response in text format
    #         rText = response[1]

    #         # testing response status codes
    #         self.assertEqual(r.status, "200 OK")
    #         self.assertNotEqual(r.status, "100 Multiple Choice")
    #         self.assertNotEqual(r.status, "300 Multiple Choice")
    #         self.assertNotEqual(r.status, "400 Bad Request")
    #         self.assertNotEqual(r.status, "404 Not Found")
    #         self.assertNotEqual(r.status, "500 Internal Server Error")

    #         # testing if navbar contents are there (should pass for all responses)
    #         assert "CoinCast" in rText
    #         assert "Home" in rText
    #         assert "Coin Forecast" in rText
    #         assert "Market Sentiment" in rText
    #         assert "Crypto Tools" in rText
    #         assert "Fear & Greed Index" in rText
    #         assert "Portfolio" in rText

    #         # testing if page contents show correctly via comparing page header
    #         assert "Market Sentiment" in rText
    #         assert "Coin Twitter Sentiment" not in rText
    #         assert "Home Page" not in rText
    #         assert "Coin Forecaster" not in rText
    #         assert "Crypto Fear and Greed" not in rText
    #         assert "Portfolio Selector" not in rText
    #         assert "Portfolio Summary" not in rText

    # testing fear and greed route
    def test_fear_and_greed(self):

        # obtaining response from fear and greed route
        response = self.app.get("/fng")

        assert b"Crypto Fear and Greed" in response.data
        assert b"Coin Twitter Sentiment" not in response.data
        assert b"Home Page" not in response.data
        assert b"Coin Forecaster" not in response.data
        assert b"Portfolio Selector" not in response.data
        assert b"Portfolio Summary" not in response.data
        assert b"Technical Analysis" not in response.data

    # testing portfolio selector route
    def test_portfolio_selector(self):

        # obtaining response from Sentiment selection route
        response = self.app.get("/portfolioSelector")

        assert b"Portfolio Selector" in response.data
        assert b"Coin Twitter Sentiment" not in response.data
        assert b"Home Page" not in response.data
        assert b"Coin Forecaster" not in response.data
        assert b"Crypto Fear and Greed" not in response.data
        assert b"Portfolio Summary" not in response.data
        assert b"Technical Analysis" not in response.data

    # testing portfolio summary route
    def test_portfolio_summary(self):

        # obtaining responses from portfolio selection route via posting fake/mock "user selected" coins to portfolio
        # then converting each response in text format to test contents of web page
        response1 = self.app.post("/portfolioSummary", data={
            "selectedCoins": ["Bitcoin", "Ethereum", "BNB", "XRP", "Terra", "Cardano", "Solana", "Avalanche",
                              "Polkadot", "Dogecoin", "Shiba Inu", "Polygon", "Cosmos", "Litecoin", "NEAR Protocol",
                              "Chainlink", "Uniswap", "TRON", "Bitcoin Cash", "Stellar"]})
        response1Text = response1.get_data(as_text=True)

        response2 = self.app.post("/portfolioSummary", data={
            "selectedCoins": ["BNB", "XRP", "Terra", "Cardano", "Solana", "Avalanche", "Polkadot", "Dogecoin",
                              "Shiba Inu", "Polygon", "Cosmos", "Litecoin"]})
        response2Text = response2.get_data(as_text=True)

        response3 = self.app.post("/portfolioSummary", data={"selectedCoins": ["Ethereum"]})
        response3Text = response3.get_data(as_text=True)

        response4 = self.app.post("/portfolioSummary", data={
            "selectedCoins": ["Bitcoin", "XRP", "Terra", "Cardano", "Cosmos", "Litecoin", "NEAR Protocol",
                              "Chainlink"]})
        response4Text = response4.get_data(as_text=True)

        response5 = self.app.post("/portfolioSummary", data={
            "selectedCoins": ["Bitcoin", "Ethereum", "BNB", "XRP", "Terra", "Cardano", "Solana", "Avalanche",
                              "Polkadot", "Dogecoin", "Shiba Inu", "Polygon", "Cosmos", "Litecoin", "NEAR Protocol",
                              "Chainlink", "Uniswap", "TRON", "Bitcoin Cash", "Stellar"]})
        response5Text = response5.get_data(as_text=True)

        response6 = self.app.post("/portfolioSummary", data={"selectedCoins": []})
        response6Text = response6.get_data(as_text=True)

        # storing all reponses in a dictionary embedded in a list
        responses = {
            "response1": [response1, response1Text],
            "response2": [response2, response2Text],
            "response3": [response3, response3Text],
            "response4": [response4, response4Text],
            "response5": [response5, response5Text],
            "response6": [response6, response6Text]
        }

        # iterating over each response to apply the same tests to each
        for response in responses.values():
            # response itself
            r = response[0]
            # response in text format
            rText = response[1]

            # testing response status codes
            self.assertEqual(r.status, "200 OK")
            self.assertNotEqual(r.status, "100 Multiple Choice")
            self.assertNotEqual(r.status, "300 Multiple Choice")
            self.assertNotEqual(r.status, "400 Bad Request")
            self.assertNotEqual(r.status, "404 Not Found")
            self.assertNotEqual(r.status, "500 Internal Server Error")

            # testing if navbar contents are there (should pass for all responses)
            assert "CoinCast" in rText
            assert "Home" in rText
            assert "Coin Forecast" in rText
            assert "Market Sentiment" in rText
            assert "Crypto Tools" in rText
            assert "Fear & Greed Index" in rText
            assert "Portfolio" in rText
            assert "Technical Analysis" in rText

            # testing if page contents show correctly via comparing page header
            assert "Portfolio Summary" in rText
            assert "Coin Twitter Sentiment" not in rText
            assert "Home Page" not in rText
            assert "Coin Forecaster" not in rText
            assert "Crypto Fear and Greed" not in rText
            assert "Portfolio Selector" not in rText
            assert "Technical Analysis" not in rText


if __name__ == '__main__':
    unittest.main()
