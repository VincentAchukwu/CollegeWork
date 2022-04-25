# Flask Test Suite for all Unit Tests

import unittest
from backendTests import TestFlaskApp
 
# executes all unit tests (test_convert, test_rates, and test_timeseries)
def my_suite():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFlaskApp))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
