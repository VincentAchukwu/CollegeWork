from Stack import Stack

def reverse_input(stack):
    # Your code here
    # Read the input
    import sys
    s = sys.stdin.readlines()
    words = [w.strip() for w in s]
    # place on the stack
    for word in words:
        stack.push(word)
    # print from the stack
    while not stack.is_empty():
        print(stack.pop())