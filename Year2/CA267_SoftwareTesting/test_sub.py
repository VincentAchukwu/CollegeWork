import unittest
from code.sub import sub

class SubTestCase(unittest.TestCase):

        def test_one(self):
            self.assertEqual(sub(1,1),0)

        def test_two(self):
            self.assertEqual(sub(1,2),-1)

        def test_three(self):
            self.assertNotEqual(sub(1,3),5)

if __name__ == '__main__':
    unittest.main()
