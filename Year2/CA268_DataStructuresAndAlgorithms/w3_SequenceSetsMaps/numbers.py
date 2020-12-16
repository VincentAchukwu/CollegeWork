def get_odd_list():
    nums = []
    n = int(input())
    while n != -1:
        if n % 2:
            nums.append(n)
        n = int(input())
    return nums

def get_evenodd_list():
    n = int(input())
    evens = []
    odds = []
    while n != -1:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
        n = int(input())
    return odds, evens

def get_sliced_lists(l):
    one = l[:-1]
    two = l[1:-1]
    three = l[::-1]
    return one, two, three

def get_counts(l):
    count = [0] * 10
    for i in l:
        count[len(i)] += 1
    return count
