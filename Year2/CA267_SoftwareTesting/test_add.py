import unittest
from code.add import add

class AddTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(add(1,1),2, "Boomer, ok")

    def test_two(self):
        self.assertEqual(add(1,2),3)

    def test_three(self):
        self.assertNotEqual(add(1,3),5)

if __name__ == '__main__':
    unittest.main()
