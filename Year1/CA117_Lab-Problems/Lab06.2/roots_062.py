import sys

def roots(a, b, c):
    if (b ** 2) >= (4 * a * c):
        r1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        r2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        return ("r1 = " + str(r1) + ", r2 = " + str(r2))
    else:
        return None

def main():
    for line in sys.stdin:
        a, b, c = line.strip().split()
        a, b, c = int(a), int(b), int(c)
        print(roots(a, b, c))

if __name__ == '__main__':
    main()
