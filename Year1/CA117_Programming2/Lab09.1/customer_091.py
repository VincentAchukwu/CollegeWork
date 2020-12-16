class Customer(object):
    discount = 0

    def __init__(self, name, balance, addr1, addr2, addr3):
        self.name = name
        self.balance = balance
        self.addr1 = addr1
        self.addr2 = addr2
        self.addr3 = addr3

    def owes(self):
        return self.balance * (1 - self.discount)

    def __str__(self):
        l = []
        l.append("{:s}".format(self.name))
        l.append("{:s}".format(self.addr1))
        l.append("{:s}".format(self.addr2))
        l.append("{:s}".format(self.addr3))
        l.append("Balance: {:.2f}".format(self.balance))
        l.append("Discount: {:.0f}%".format(self.discount * 100))
        l.append("Amount due: {:.2f}".format(self.owes()))
        return "\n".join(l)

class ValuedCustomer(Customer):
    discount = 0.1
