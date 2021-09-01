# Flask Unit Tests for Rates and Historic Rates

import unittest, requests
from datetime import datetime

class RatesTestCase(unittest.TestCase):

    # initialising Flask test client
    # essentially testing various inputs and passing them into flask server as parameters
    def setUp(self):

        # expected: OK
        self.base1, self.date1, self.codes1 = "", "", "EUR"
        self.urlOne = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base1, self.date1, self.codes1)

        # expected: OK
        self.base2, self.date2, self.codes2 = "", "", "gbp uSd bTc"
        self.urlTwo = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base2, self.date2, self.codes2)

        # expected: FAILED
        self.base3, self.date3, self.codes3 = "", "", "hello world"
        self.urlThree = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base3, self.date3, self.codes3)

        # expected: FAILED
        self.base4, self.date4, self.codes4 = "", "", "100 70"
        self.urlFour = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base4, self.date4, self.codes4)

        # Fixer API has no record of USD rate on this date
        # expected: FAILED
        self.base5, self.date5, self.codes5 = "", "1999-01-01", "USD"
        self.urlFive = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base5, self.date5, self.codes5)

        # expected: OK
        todaysDate = datetime.today().strftime("%Y-%m-%d")
        self.base6, self.date6, self.codes6 = "", todaysDate, "eur usd"
        self.urlSix = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base6, self.date6, self.codes6)

        # expected: OK
        self.base7, self.date7, self.codes7 = "", "2012-11-05", "INR AUD"
        self.urlSeven = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base7, self.date7, self.codes7)

        # expected: FAILED (this test would be OK by 20/09/2040, 
        # essentially, unit test would have to change by then)
        self.base8, self.date8, self.codes8 = "", "2040-09-20", "EUR"
        self.urlEight = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base8, self.date8, self.codes8)

        # expected: FAILED
        self.base9, self.date9, self.codes9 = "", "1998-12-31", "JPY"
        self.urlNine = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base9, self.date9, self.codes9)

        # expected: FAILED
        self.base10, self.date10, self.codes10 = "", "2021-1-1", "eur LTL"
        self.urlTen = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base10, self.date10, self.codes10)

        # expected: FAILED
        self.base11, self.date11, self.codes11 = "", "2021-1-01", "gbp btc"
        self.urlEleven = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base11, self.date11, self.codes11)

        # expected: FAILED
        self.base12, self.date12, self.codes11 = "", "2020 3 1", "OMG"
        self.urlTwelve = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base12, self.date12, self.codes11)

        # expected: OK
        self.base13, self.date13, self.codes13 = "btc", todaysDate, "AOA"
        self.urlThirteen = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base13, self.date13, self.codes13)

        # expected: OK
        self.base14, self.date14, self.codes14 = "eur", "2020-02-01", "gbp"
        self.urlFourteen = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base14, self.date14, self.codes14)

        # expected: FAILED
        self.base15, self.date15, self.codes15 = "omg", "2020-02-01", "gbp"
        self.urlFifteen = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base15, self.date15, self.codes15)

        # expected: FAILED
        self.base16, self.date16, self.codes16 = "GB", "2011-3-22", "USD"
        self.urlSixteen = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base16, self.date16, self.codes16)

        # expected: FAILED
        self.base17, self.date17, self.codes17 = "euR", "2014-9-20", "USD BTC"
        self.urlSeventeen = "https://currencyapp200.pythonanywhere.com/api/rates?base={}&date={}&rates={}".format(
            self.base17, self.date17, self.codes17)
        
        # then separate the url's with valid parameters from the invalid ones
        self.ok = [self.urlOne, self.urlTwo, self.urlSix, self.urlSeven, self.urlThirteen, self.urlFourteen]
        self.failed = [self.urlThree, self.urlFour, self.urlFive, self.urlEight, self.urlNine, self.urlTen, self.urlEleven, self.urlTwelve, self.urlFifteen, self.urlSixteen, self.urlSeventeen]

    # using loop to run same tests on all URL's with VALID parameters
    def test_response_ok(self):
        # used for tracking list index for output
        i = 0
        # iterating over URLs
        for url in self.ok:
            # displaying on terminal which URL in self.ok list is being tested
            print("Testing CORRECT RATES params {}".format(i))
            # getting response of first URL
            response = requests.get(url)

            # checking content type
            self.assertEqual(response.headers["content-type"], "application/json")
            self.assertNotEqual(response.headers["content-type"], "html/text")

            # checking status code
            self.assertEqual(response.status_code , 200)
            self.assertNotEqual(response.status_code , 500)
            self.assertNotEqual(response.status_code , 404)

            # checking JSON response has correct content inside
            self.assertTrue("requestedRates" in response.json())
            self.assertFalse("requestedRates" not in response.json())
            self.assertTrue(len(response.json()) > 0)
            self.assertFalse(len(response.json()) <= 0)

            # checking that appropriate keys are in the dictionary response
            self.assertTrue("key" in response.json()["requestedRates"][0])
            self.assertFalse("key" not in response.json()["requestedRates"][0])
            self.assertTrue("rate" in response.json()["requestedRates"][0])
            self.assertFalse("rate" not in response.json()["requestedRates"][0])
            i += 1

    # using loop to run same tests on all URL's with INVALID parameters
    def test_response_failed(self):
        # used for tracking list index for output
        i = 0
        # iterating over URLs
        for url in self.failed:
            # displaying on terminal which URL in self.failed list is being tested
            print("Testing INCORRECT RATES params {}".format(i))
            # getting response of first URL
            response = requests.get(url)

            # checking content type
            self.assertEqual(response.headers["content-type"], "application/json")
            self.assertNotEqual(response.headers["content-type"], "html/text")

            # checking status code
            self.assertEqual(response.status_code , 200)
            self.assertNotEqual(response.status_code , 500)
            self.assertNotEqual(response.status_code , 404)

            # checking JSON response has correct content inside
            self.assertTrue("requestedRates" in response.json())
            self.assertFalse("requestedRates" not in response.json())
            self.assertTrue(len(response.json()) > 0)
            self.assertFalse(len(response.json()) <= 0)

            # checking that appropriate keys are in the dictionary response
            self.assertTrue("key" in response.json()["requestedRates"][0])
            self.assertFalse("key" not in response.json()["requestedRates"][0])

            # since these url's don't have correct parameters for fixer.io, "invalid" will be outputted
            self.assertTrue("rate" not in response.json()["requestedRates"][0])
            self.assertFalse("rate" in response.json()["requestedRates"][0])
            self.assertEqual(response.json()["requestedRates"][0]["key"], "invalid")
            self.assertNotEqual(response.json()["requestedRates"][0]["key"], "")
            i += 1

if __name__ == '__main__':
    unittest.main()
