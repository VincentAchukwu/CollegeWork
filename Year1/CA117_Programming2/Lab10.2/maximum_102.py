def maximum(l):
    if len(l) == 1:
        return l[0]
    return l[0] if l[0] > maximum(l[1:]) else maximum(l[1:])
