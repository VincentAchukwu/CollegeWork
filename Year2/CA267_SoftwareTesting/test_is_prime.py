import unittest
from code.primes import is_prime

class PrimesTestCase(unittest.TestCase):

    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_four_prime(self):
        self.assertFalse(is_prime(4))

    def test_is_three_prime(self):
        self.assertTrue(is_prime(3))
       
                   
if __name__ == '__main__':
    unittest.main()

        
