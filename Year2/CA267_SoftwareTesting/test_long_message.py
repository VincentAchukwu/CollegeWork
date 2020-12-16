import unittest

class LongMessageTestCase(unittest.TestCase):

    def test_use_long_message(self):
        # long message is the mechanism for printing a custom message
        # in this case: "two numbers are equal"
        actual_value = 4
        expected_value = 5
        self.assertNotEqual(actual_value, expected_value, "two numbers are equal")

if __name__ == '__main__':
    unittest.main()
