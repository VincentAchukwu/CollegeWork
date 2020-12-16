def rprint(a, b):
    print(a)
    if a >= b - 1:
        return a
    return rprint(a + 1, b)
