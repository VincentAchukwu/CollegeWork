import sys
import math
class Stack(object):
    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        if len(self.l) != 0:
            return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)


def addition(x, y):
   return x + y

def subtraction(x, y):
   return x - y

def multiplication(x, y):
   return x * y

def division(x, y):
   return x / y

def negate(x):
   return -x

def squareroot(x):
   return math.sqrt(x)

binops = {
   "+": addition,
   "-": subtraction,
   "*": multiplication,
   "/": division,
}

 uniops = {
   "n": negate,
   "r": squareroot,
}

def calculator(token):
    s = Stack()
    tokens = token.split()
    for token in tokens:
        try:
            if token in binops:
                y = s.pop()
                x = s.pop()
                result = binops[token](x, y)
                s.push(result)
            elif token in uniops:
                x = s.pop()
                result = uniops[token](x)
                s.push(result)
            else:
                s.push(float(token))
        except TypeError:
            pass
    return s.l[0]
