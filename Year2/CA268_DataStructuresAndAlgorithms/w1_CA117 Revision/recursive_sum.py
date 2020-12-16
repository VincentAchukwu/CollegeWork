def sumto(a, b):
    if a >= b:
        return 0
    return a + sumto(a + 1, b)
