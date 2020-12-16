class Stack:
 def __init__(self, capacity = 10):
    self.data = [0] * capacity
    self.top = 0
 def is_empty(self):
     return self.top == 0
 def push(self, item):
    if self.top < len(self.data):
        self.data[self.top] = item
    else:
        raise Exception("The Stack is full!")
    self.top += 1
 def pop(self):
    if self.is_empty():
        return None
    else:
        self.top -= 1
        return self.data[self.top]


def check_brackets(line):
    d = {")": "("}
    s = Stack()
    for c in line:
        if c in d.values():
            s.push(c)
        if c in d.keys():
            if d[c] != s.pop():
                return False
    return s.is_empty()
    