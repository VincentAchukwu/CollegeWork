def set_intersection(s1, s2):
    return s1 & s2

def set_stuff(a, b):
    return a.union(b), a.issubset(b), a.issuperset(b)

def unique_list(l):
    return list(set(l))