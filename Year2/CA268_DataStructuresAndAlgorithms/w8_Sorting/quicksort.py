#V1
def partition(lst, lo, hi):
    global comp, moves
    part = lo
    while lo < hi:
        comp += 1
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
            comp += 1
        comp += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1
            comp += 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            moves += 3

    # Swap part into position
    comp += 1
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        moves += 3
        
    return hi

def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    global comp, moves
    comp = 0
    moves = 0
    rec_qsort(lst, 0, len(lst) - 1)
    return comp, moves

#V2
def partition(lst, lo, hi):
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        
    return hi

def rec_qsort(lst, lo, hi): #rec=1 as additonal argument for testing recursive depth
    # global rec_lst
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)
        rec_lst.append(rec())

def qsort(lst):
    # global rec_lst    testing recursive depth
    # rec_lst = []
    rec_qsort(lst, 0, len(lst) - 1)
    # return max(rec_lst)