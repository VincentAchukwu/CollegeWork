# This is an example of adding unit tests to unit test suite
# It is for demonstration purposes only as  typically, many more unit test cases
# from multiple different sources would be added to a test suite. In this case we
# only add a single set of unit tests to the test suite

import unittest
 
from test_sub import SubTest
 
 
def my_suite():
    suite = unittest.TestSuite() #instance of Testsuite
    result = unittest.TestResult()#instance of Testresult
    suite.addTest(unittest.makeSuite(SubTest))# addTest is a keyword
    #SubTest class contains unit tests in file "test_sub.py" to test my implementation 
    # of substraction    
    runner = unittest.TextTestRunner()
    print(runner.run(suite)) #execute the test in a test runner and print the result
 
my_suite()
