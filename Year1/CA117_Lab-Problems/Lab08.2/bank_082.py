class BankAccount(object):
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0.00):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.number = BankAccount.next_account_number
        self.lodgements = BankAccount.total_lodgements
        BankAccount.next_account_number += 1

    def lodge(self, l):
        self.balance += l
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        self.balance *= 1 + BankAccount.interest_rate

    def __iadd__(self, money):
        BankAccount.total_lodgements += 1
        self.balance += money
        return self

    def __str__(self):
        l = []
        l.append("Name: {:s} {:s}".format(self.forename, self.surname))
        l.append("Account number: {:d}".format(self.number))
        l.append("Balance: {:.2f}".format(self.balance))
        return "\n".join(l)
