import sys

def swap_keys_values(d):
    nd = {}
    for k, v in d.items():
        nd[v] = k
    return nd

if __name__ == '__main__':
    main()
