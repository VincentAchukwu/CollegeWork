# Flask Test Suite for all Unit Tests

import unittest
from test_convert import ConvertTestCase
from test_rates import RatesTestCase
from test_timeseries import TimeseriesTestCase
 
# executes all unit tests (test_convert, test_rates, and test_timeseries)
def my_suite():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ConvertTestCase))
    suite.addTest(unittest.makeSuite(RatesTestCase))
    suite.addTest(unittest.makeSuite(TimeseriesTestCase))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
