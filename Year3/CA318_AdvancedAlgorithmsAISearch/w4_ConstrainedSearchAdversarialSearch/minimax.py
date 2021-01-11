class Node:
    def __init__(self, v = -1, l=None, m=None, r=None):
        self.val = v
        self.left = l
        self.right = r
        self.mid = m

    def is_terminal(self):
        return self.left == None and self.mid == None and self.right == None

    def evaluation(self):
        return self.val

class Tree:
    def __init__(self):
        self.root = None

def minimax(tree):

    a = []  # recusively adds terminal nodes to list
    lst = minimaxR(tree.root, a)    # created new list for intervals part below
    intervals = [lst[i:i+3] for i in range(0, len(lst), 3)]     # makes list in intervals of 3

    # finding the depth (we're told depth would range within 2-10)
    # num nodes at depth = 3 ** depth
    for i in range(0, 11):
        # lst is the num of nodes at lowest depth
        if len(lst) == (3 ** i):
            depth = i
            break

    # (draw graph for clearer understanding)
    # excluding the last depth (i.e depth - 1) since nodes @ last depth are terminal
    for minMax in range(depth - 1, -1, -1):
        # MAX part @ depths divisible by 2, else MIN part
        if minMax % 2 == 1:
            tempIntervals = [min(nodes) for nodes in intervals]
        else:
            tempIntervals = [max(nodes) for nodes in intervals]

        # updates current intervals into 3 again
        intervals = [tempIntervals[i:i+3] for i in range(0, len(tempIntervals), 3)]

    return intervals[0][0]  # since it's a list within a list with only one value


def minimaxR(ptr, a):

    if not ptr.is_terminal():
        leftTraversal = minimaxR(ptr.left, a)
        midTraversal = minimaxR(ptr.mid, a)
        rightTraversal = minimaxR(ptr.right, a)
    else:
        a.append(ptr.evaluation())

    return a
