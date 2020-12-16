def reverse_list(l):
    if len(l) == 0 or len(l) == 1:
        return l
    return reverse_list(l[1:]) + [l[0]]
