import unittest
from test_add import AddTestCase
from test_is_prime import PrimesTestCase
from test_sub import SubTestCase
from test_emp import EmpTestCase
from test_long_message import LongMessageTestCase
from test_fact import FactTestCase
 
def my_suite():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AddTestCase))
    suite.addTest(unittest.makeSuite(PrimesTestCase))
    suite.addTest(unittest.makeSuite(SubTestCase))
    suite.addTest(unittest.makeSuite(EmpTestCase))
    suite.addTest(unittest.makeSuite(LongMessageTestCase))
    suite.addTest(unittest.makeSuite(FactTestCase))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
