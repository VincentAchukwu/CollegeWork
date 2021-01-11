class Item(object):
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def ks_greedy(initial_capacity, items):
    assert initial_capacity >= 0

    # did it this way to convert list of items to list of tuples
    updatedItems = []
    for item in items:
        updatedItems.append((item.value, item.weight))

    updatedItems = sorted(updatedItems, reverse=True)
    total_value = 0
    i = 0
    while i < len(updatedItems):
        # identifying value and weight from list of tuples
        value = updatedItems[i][0]
        weight = updatedItems[i][1]
        # if the current weight < capacity, we update total_value
        # then decrement capacity left by current weight
        if weight <= initial_capacity:
            total_value += value
            initial_capacity -= weight
            i = 0   # resets loop (since we're looking for largest item weight smaller than capacity)
        else:
            i += 1  # else we know current weight is too big, get next item

    return total_value

def main():
    # print(ks_greedy(10, [(20, 5), (300, 11), (4, 2)]))
    # print(ks_greedy(10, [Item(20, 5), Item(300, 11), Item(4, 2)]))
    print(ks_greedy(41, [Item(20, 5), Item(300, 11), Item(4, 2)]))

if __name__ == '__main__':
    main()
