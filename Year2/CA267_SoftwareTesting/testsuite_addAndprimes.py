import unittest
 
from test_add import AddTestCase
from test_is_prime import PrimesTestCase
 
 
def my_suite():
    suite = unittest.TestSuite() #instance of Testsuite
    suite.addTest(unittest.makeSuite(AddTestCase))# addTest is a keyword
    suite.addTest(unittest.makeSuite(PrimesTestCase))
    runner = unittest.TextTestRunner()
    print(runner.run(suite)) # run the suite and print out the results
 
my_suite()
