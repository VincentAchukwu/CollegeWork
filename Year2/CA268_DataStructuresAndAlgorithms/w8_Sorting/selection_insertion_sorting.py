### INSERTION SORT ###

#V1
def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    comp_count = 0
    swap_count = 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        comp_count += 1
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            i -= 1
            if i > 0:
                comp_count += 1
            swap_count += 1

    return comp_count, swap_count

#V2
def insertion_sort(lst):
    comp_count = 0
    moves_count = 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        moves_count += 1
        comp_count += 1
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1] # Make space for the item
            i -= 1
            moves_count += 1
            if i != 0:
                comp_count += 1
        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        moves_count += 1

    return comp_count, moves_count


#V3
def insertion_sort(lst):
    comp_count = 0
    moves_count = 0
    if len(lst) == 0:
        return

    # Find the smallest element
    min_index = 0
    for i in range(1, len(lst)):
        comp_count += 1
        # moves_count += 1
        if lst[i] < lst[min_index]:
            # moves_count += 1
            min_index = i

    # Move smallest to the front (swap elements min_index and 0)
    lst[0], lst[min_index] = lst[min_index], lst[0]
    moves_count += 3

    # Now, with the smallest in the front, we don't need to check i in the inner loop
    
    # At each pass ensure that that section is sorted (start at 2, cos smallest already in position).
    for todo in range(2, len(lst)):
        # Find correct position for lst[todo]
        store = lst[todo]
        moves_count += 1
        i = todo
        while store < lst[i-1]: # Don't need to check i > 0
            lst[i] = lst[i-1] # Make space for the item
            moves_count += 1
            comp_count += 1
            i -= 1
        comp_count += 1
        lst[i] = store  # Found the place for this item, plonk it in
        moves_count += 1
    return comp_count, moves_count

### SELECTION SORT ###

#V1
""" Selection sort algorithm """
def selection_sort(lst):
    moves = 0
    comp = 0
    for i in range(len(lst) - 1):
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):
            comp += 1
            if lst[j] < lst[min_index]:
                min_index = j
        # place smallest at the beginning (swap min index with i)
        lst[i], lst[min_index] = lst[min_index], lst[i]
        moves += 3
    return comp, moves

#V2
""" Selection sort algorithm """
def selection_sort(lst):
    moves = 0
    comp = 0
    for i in range(len(lst) - 1):
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):
            comp += 1
            if lst[j] < lst[min_index]:
                min_index = j
        # place smallest at the beginning (swap min index with i)
        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i] # Don't swap if already in position
            moves += 3
    return comp, moves

#V3
def selection_sort(lst):
    moves = 0
    comp = 0
    lo = 0
    hi = len(lst) - 1
    while lo < hi:
        min_index = lo
        max_index = lo
        for j in range(lo + 1, hi + 1):
            comp += 2
            if lst[j] < lst[min_index]:
                min_index = j
                comp -= 1
            elif lst[j] > lst[max_index]: # maybe >= to get stable sort
                max_index = j
                # comp += 1
            # else:
            #     comp += 1 #same thing..
        if max_index == lo:
            max_index = min_index   # We will be moving lst[lo] to min_index, so update max_index first

        # swap min index with lo ... place smallest at the first
        lst[lo], lst[min_index] = lst[min_index], lst[lo]
        moves += 3
        # swap max index with hi ... place largest at the end
        lst[hi], lst[max_index] = lst[max_index], lst[hi]
        moves += 3
        lo += 1
        hi -= 1
    return comp, moves