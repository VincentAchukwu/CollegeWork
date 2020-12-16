import sys

def swap_unique_keys_values(d):
    return dict([(v, k) for (k, v) in d.items() if list(d.values()).count(v) == 1])


if __name__ == '__main__':
    main()
