import sys

def build_d(filename):
    food = {}
    with open(filename, "r") as f:
        for line in f:
            mapping = line.strip().split()
            food[" ".join(mapping[0:-1])] = int(mapping[-1])
    return food

def sorter(t):
    return t[1]

def main():
    pass
    nd = {}
    d = build_d(sys.argv[1])
    for line in sys.stdin:
        total_cal = 0
        tokens = line.strip().split(",")
        name = tokens[0]
        foods = tokens[1:]
        for f in foods:
            if f in d.keys():
                total_cal = total_cal + d[f]
            else:
                total_cal = total_cal + 100
        nd[name] = total_cal

    max_k_width = len(max(nd.keys(), key=len))
    max_v_width = len(str(max(nd.values())))
    for k, v in sorted(nd.items(), key=sorter):
        print("{:>{:d}s} : {:{:d}d}".format(k, max_k_width, v, max_v_width))

if __name__ == '__main__':
    main()
