def make_map():
    students = {}
    n = input()
    while n:
        info = n.strip().split()
        name, mark = info[0], info[1]
        students[name] = mark
        n = input()
    return students