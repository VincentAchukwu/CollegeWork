import math

class Item(object):
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def ks_greedy(initial_capacity, items):
    assert initial_capacity >= 0

    total_value = 0
    i = 0
    while i < len(items):
        # identifying value and weight from list of tuples
        value = items[i][0]
        weight = items[i][1]
        # if the current weight < capacity, we update total_value
        # then decrement capacity left by current weight
        if weight <= initial_capacity:
            total_value += value
            initial_capacity -= weight
            i = 0   # resets loop (since we're looking for largest item weight smaller than capacity)
        else:
            i += 1  # else we know current weight is too big, get next item

    return total_value

def dp_knapsack(initial_capacity, items):
    assert initial_capacity >= 0
    # Initialise memo to be - infinity for each of capacity + 1 values
    memo = [-math.inf] * (initial_capacity+1)    # Had a BUG here ... initially + infinity
   
        # did it this way to convert list of items to list of tuples
    updatedItems = []
    for item in items:
        updatedItems.append((item.value, item.weight))

    updatedItems.sort(reverse=True)

    # for item in updatedItems:
    #     print("Value = {}, Weight = {}".format(item[0], item[1]))

    memo[0] = 0
    for currCapacity in range(1, len(memo)):
        memo[currCapacity] = max([item[0] + memo[currCapacity - item[1]] for item in updatedItems if item[1] <= initial_capacity])
        # memo[currCapacity] = ks_greedy(currCapacity, updatedItems)

    return memo

def main():
    # print(dp_knapsack(10, [Item(20, 5), Item(300, 11), Item(4, 2)]))
    print(dp_knapsack(41, [Item(20, 5), Item(300, 11), Item(4, 2)]))

if __name__ == '__main__':
    main()
