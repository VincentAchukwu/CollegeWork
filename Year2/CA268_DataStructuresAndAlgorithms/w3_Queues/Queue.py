#
#  Create a queue relying on a Stack. Actually Two Stacks.
#
#  The Stack ADT has three methods:
#     isempty(), push() and pop()
#
from Stack import Stack

class Queue:
    def __init__(self):
        # Initialise the queue
        # YOUR CODE HERE
        self.item1 = Stack()
        self.item2 = Stack()
        
    def isempty(self):
        # YOUR CODE HERE
        return self.item1.isempty() and self.item2.isempty()

    def enqueue(self, item):
        # YOUR CODE HERE
        self.item1.push(item)

    def dequeue(self):
        # YOUR CODE HERE
        if self.item2.isempty():
            while not self.item1.isempty():
                self.item2.push(self.item1.pop())
        return self.item2.pop()
