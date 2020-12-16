import unittest
from code.fact import fact

class FactTestCase(unittest.TestCase):

	def test_fact3(self):
		self.assertEqual(fact(3), 6)

	def test_fact5(self):
		self.assertNotEqual(fact(5), 121, "<--foookin boomer roight durr")

	def test_fact6(self):
		self.assertEqual(fact(6), 720)

if __name__ == '__main__':
	unittest.main()
