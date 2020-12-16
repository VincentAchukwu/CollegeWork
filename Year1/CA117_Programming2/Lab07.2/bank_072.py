class BankAccount(object):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, d):
        self.balance += d

    def withdraw(self, w):
        if self.balance - w >= 0:
            self.balance -= w
        else:
            print("Insufficient funds available")

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self.balance)
