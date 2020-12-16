def maximum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] if lst[0] >= maximum(lst[1:]) else maximum(lst[1:])
