import sys

def l2d(s):
    d = {}
    animals, num = [line.strip() for line in sys.stdin]
    for i, a in enumerate(animals.split()):
        d[a] = num.split()[i]
    return d

def main():
    d = l2d(sys.stdin)
    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
