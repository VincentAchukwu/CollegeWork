import sys

def build_dictionary(filename):
    d = {}
    with open(filename, "r") as f:
        for line in f:
            mapping = line.strip().split()
            d[mapping[0]] = int(mapping[1])
        return d

def extract_range(d, low, high):
    nd = {}
    for k, v in d.items():
        if low <= v <= high:
            nd[k] = v
    return nd

if __name__ == '__main__':
    main()
