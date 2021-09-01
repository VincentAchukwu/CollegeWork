# Flask Unit Tests for Time series

import unittest, requests

class TimeseriesTestCase(unittest.TestCase):

    # initialising Flask test client
    # essentially testing various inputs and passing them into flask server as parameters
    def setUp(self):

        # expected: OK
        self.fromCurr1, self.toCurr1 = "btc", "eur"
        self.urlOne = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr1, self.toCurr1)

        # expected: OK
        self.fromCurr2, self.toCurr2 = "UsD", "bTc"
        self.urlTwo = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr2, self.toCurr2)

        # expected: OK
        self.fromCurr3, self.toCurr3 = "MDL", "LTL"
        self.urlThree = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr3, self.toCurr3)

        # expected: FAILED
        self.fromCurr4, self.toCurr4 = "gb", "eur"
        self.urlFour = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr4, self.toCurr4)

        # expected: FAILED
        self.fromCurr5, self.toCurr5 = "BTC", "LV"
        self.urlFive = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr5, self.toCurr5)

        # expected: OK
        self.fromCurr6, self.toCurr7 = "GBP", "CAD"
        self.urlSix = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr6, self.toCurr7)

        # expected: OK
        self.fromCurr7, self.toCurr7 = "mxn", "mwk"
        self.urlSeven = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr7, self.toCurr7)

        # expected: OK
        self.fromCurr8, self.toCurr8 = "EUr", "gBP"
        self.urlEight = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr8, self.toCurr8)

        # expected: FAILED
        self.fromCurr9, self.toCurr9 = "omg", "eur"
        self.urlNine = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr9, self.toCurr9)

        # expected: OK
        self.fromCurr10, self.toCurr100 = "uSd", "cAD"
        self.urlTen = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr10, self.toCurr100)

        # expected: FAILED
        self.fromCurr11, self.toCurr112 = "a", "B"
        self.urlEleven = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr11, self.toCurr112)

        # expected: FAILED
        self.fromCurr12, self.toCurr122 = "123", "97"
        self.urlTwelve = "https://currencyapp200.pythonanywhere.com/api/timeSeries?fromCurr={}&toCurr={}".format(
            self.fromCurr12, self.toCurr122)

        # then separate the url's with valid parameters from the invalid ones
        self.ok = [self.urlOne, self.urlTwo, self.urlThree, self.urlSix, self.urlSeven, self.urlEight, self.urlTen]
        self.failed = [self.urlFour, self.urlFive, self.urlNine, self.urlEleven, self.urlTwelve]

    # then using a loop, run tests on each url

    # using loop to run same tests on all URL's with VALID parameters
    def test_response_ok(self):
        # used for tracking list index for output
        i = 0
        # iterating over URL's
        for url in self.ok:
            # displaying on terminal which URL in self.ok list is being tested
            print("Testing CORRECT TIMESERIES params {}".format(i))
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
            self.assertTrue("requestedTimeSeries" in response.json())
            self.assertFalse("requestedTimeSeries" not in response.json())
            self.assertTrue(len(response.json()) > 0)
            self.assertFalse(len(response.json()) <= 0)

            # checking that appropriate keys are in the dictionary response
            self.assertTrue("key" in response.json()["requestedTimeSeries"][0])
            self.assertFalse("key" not in response.json()["requestedTimeSeries"][0])
            self.assertTrue("code" in response.json()["requestedTimeSeries"][0])
            self.assertFalse("code" not in response.json()["requestedTimeSeries"][0])
            self.assertTrue("rate" in response.json()["requestedTimeSeries"][0])
            self.assertFalse("rate" not in response.json()["requestedTimeSeries"][0])
            i += 1

    # using loop to run same tests on all URL's with INVALID parameters
    def test_response_failed(self):
        # used for tracking list index for output
        i = 0
        # iterating over URL's
        for url in self.failed:
            # displaying on terminal which URL in self.failed list is being tested
            print("Testing INCORRECT TIMESERIES params {}".format(i))
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
            self.assertTrue("requestedTimeSeries" in response.json())
            self.assertFalse("requestedTimeSeries" not in response.json())
            self.assertTrue(len(response.json()) > 0)
            self.assertFalse(len(response.json()) <= 0)

            # checking that appropriate keys are in the dictionary response
            self.assertTrue("key" in response.json()["requestedTimeSeries"][0])
            self.assertFalse("key" not in response.json()["requestedTimeSeries"][0])
            self.assertTrue("code" not in response.json()["requestedTimeSeries"][0])
            self.assertFalse("code" in response.json()["requestedTimeSeries"][0])
            self.assertTrue("rate" not in response.json()["requestedTimeSeries"][0])
            self.assertFalse("rate" in response.json()["requestedTimeSeries"][0])

            # since these url's don't have correct parameters for fixer.io, "invalid" will be outputted
            self.assertEqual(response.json()["requestedTimeSeries"][0]["key"], "invalid")
            self.assertNotEqual(response.json()["requestedTimeSeries"][0]["key"], "")
            self.assertNotEqual(response.json()["requestedTimeSeries"][0]["key"], "INVALID")
            self.assertNotEqual(response.json()["requestedTimeSeries"][0]["key"], 404)
            self.assertNotEqual(response.json()["requestedTimeSeries"][0]["key"], "invalid.")
            i += 1

if __name__ == '__main__':
    unittest.main()
