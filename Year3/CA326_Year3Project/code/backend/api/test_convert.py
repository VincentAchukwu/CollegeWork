# Flask Unit Tests for Currency Conversions

import unittest, requests

class ConvertTestCase(unittest.TestCase):

    # initialising Flask test client
    # essentially testing various inputs and passing them into flask server as parameters
    def setUp(self):

        # expected: OK
        self.fromCurr1, self.toCurr1, self.amount1 = "btc", "eur", "20"
        self.urlOne = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr1, self.toCurr1, self.amount1)

        # expected: OK
        self.fromCurr2, self.toCurr2, self.amount2 = "UsD", "bTc", "64.20"
        self.urlTwo = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr2, self.toCurr2, self.amount2)

        # expected: OK
        self.fromCurr3, self.toCurr3, self.amount3 = "MDL", "LTL", "2."
        self.urlThree = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr3, self.toCurr3, self.amount3)

        # expected: FAILED
        self.fromCurr4, self.toCurr4, self.amount4 = "EU", "gbp", "25"
        self.urlFour = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr4, self.toCurr4, self.amount4)

        # expected: FAILED
        self.fromCurr5, self.toCurr5, self.amount5 = "BTC", "LV", "11000"
        self.urlFive = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr5, self.toCurr5, self.amount5)

        # expected: FAILED
        self.fromCurr6, self.toCurr7, self.amount7 = "GBP", "CAD", "0"
        self.urlSix = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr6, self.toCurr7, self.amount7)

        # expected: FAILED
        self.fromCurr7, self.toCurr7, self.amount7 = "mxn", "mwk", "0.0"
        self.urlSeven = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr7, self.toCurr7, self.amount7)

        # expected: OK
        self.fromCurr8, self.toCurr8, self.amount8 = "EUr", "gBP", "100"
        self.urlEight = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr8, self.toCurr8, self.amount8)

        # expected: FAILED
        self.fromCurr9, self.toCurr9, self.amount9 = "omg", "eur", "0"
        self.urlNine = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr9, self.toCurr9, self.amount9)

        # expected: OK
        self.fromCurr10, self.toCurr10, self.amount10 = "uSd", "cAD", "590"
        self.urlTen = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr10, self.toCurr10, self.amount10)

        # expected: FAILED
        self.fromCurr11, self.toCurr11, self.amount12 = "a", "B", "25"
        self.urlEleven = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr11, self.toCurr11, self.amount12)

        # expected: FAILED
        self.fromCurr12, self.toCurr12, self.amount12 = "123", "987", "25"
        self.urlTwelve = "https://currencyapp200.pythonanywhere.com/api/conversions?fromCurr={}&toCurr={}&amount={}".format(
            self.fromCurr12, self.toCurr12, self.amount12)

        # then separate the url's with valid parameters from the invalid ones
        self.ok = [self.urlOne, self.urlTwo, self.urlThree, self.urlEight, self.urlTen]
        self.failed = [self.urlFour, self.urlFive, self.urlSix, self.urlSeven, self.urlNine, self.urlEleven, self.urlTwelve]

    # then using a loop, run tests on each url

    # using loop to run same tests on all URL's with VALID parameters
    def test_response_ok(self):
        # used for tracking list index for output
        i = 0
        # iterating over URL's
        for url in self.ok:
            # displaying on terminal which URL in self.ok list is being tested
            print("Testing CORRECT CONVERSION params {}".format(i))
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
            self.assertTrue("requestedConversion" in response.json())
            self.assertFalse("requestedConversion" not in response.json())
            self.assertTrue(len(response.json()) > 0)
            self.assertFalse(len(response.json()) <= 0)

            # checking that appropriate keys are in the dictionary response
            self.assertTrue("key" in response.json()["requestedConversion"][0])
            self.assertFalse("key" not in response.json()["requestedConversion"][0])
            i += 1

    # using loop to run same tests on all URL's with INVALID parameters
    def test_response_failed(self):
        # used for tracking list index for output
        i = 0
        # iterating over URL's
        for url in self.failed:
            # displaying on terminal which URL in self.failed list is being tested
            print("Testing INCORRECT CONVERSION params {}".format(i))
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
            self.assertTrue("requestedConversion" in response.json())
            self.assertFalse("requestedConversion" not in response.json())
            self.assertTrue(len(response.json()) > 0)
            self.assertFalse(len(response.json()) <= 0)

            # checking that appropriate keys are in the dictionary response
            self.assertTrue("key" in response.json()["requestedConversion"][0])
            self.assertFalse("key" not in response.json()["requestedConversion"][0])

            # since these url's don't have correct parameters for fixer.io,
            # "invalid" will be outputted in the dictionary
            self.assertEqual(response.json()["requestedConversion"][0]["key"], "invalid")
            self.assertNotEqual(response.json()["requestedConversion"][0]["key"], "")
            i += 1

if __name__ == '__main__':
    unittest.main()
