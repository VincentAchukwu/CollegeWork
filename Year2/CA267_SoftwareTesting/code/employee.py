class Employee(object):

    raise_amt = 1.05
    deduction = 1000

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.email = email

    # @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    # @property
    def email(self):
        return "{}.{}@gmail.com".format(self.fname, self.lname)

    def applyRaise(self):
        self.salary = int(self.salary * self.raise_amt)

    def applyDeduction(self):
        self.salary = self.salary - deduction
