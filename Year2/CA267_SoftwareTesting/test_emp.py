import unittest
from code.employee import Employee

class EmpTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.emp1 = Employee("Young", "Vinny", 20000)

    def tearDown(self):
        print("tearDown\n")

    def test_fullname(self):
        print("test full name")

        self.assertEqual(self.emp1.fullname(), 'Young Vinny')

    def test_email(self):
        print("test email")

        self.assertEqual(self.emp1.email(), 'Young.Vinny@gmail.com')

        self.emp1.fname = "Tony"
        self.assertEqual(self.emp1.email(), "Tony.Vinny@gmail.com")
        self.assertNotEqual(self.emp1.email(), "Young.Vinny@gmail.com")

        self.emp1.lname = "Bob"
        self.assertEqual(self.emp1.email(), "Tony.Bob@gmail.com")
        self.assertNotEqual(self.emp1.email(), "Young.Bob@gmail.com")

    def test_applyRaise(self):
        print("test applyRaise")

        self.assertEqual(self.emp1.salary, 20000)

        self.emp1.applyRaise()
        self.assertEqual(self.emp1.salary, 21000)

if __name__ == '__main__':
    unittest.main()
