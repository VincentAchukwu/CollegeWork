import sys

def is_x(n):
    a = []
    for i in n:
        if not i % 3:
           a.append("X")
        else:
           a.append(i)
    return a

def isprime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def numcomp(n):
    numlist = []
    for i in range(1, n + 1):
        numlist.append(int(i))
    print("Multiples of 3: {}".format([w for w in numlist if not w % 3]))
    print("Multiples of 3 squared: {}".format([w * w for w in numlist if not w % 3]))
    print("Multiples of 4 doubled: {}".format([w * 2 for w in numlist if not w % 4]))
    print("Multiples of 3 or 4: {}".format([w for w in numlist if (not w % 3 or not w % 4)]))
    print("Multiples of 3 and 4: {}".format([w for w in numlist if not (w % 3 or w % 4)]))
    print("Multiples of 3 replaced: {}".format(is_x(numlist)))
    print("Primes: {}".format([w for w in numlist if isprime(w)]))


def main():
    numcomp(int(sys.argv[1]))


if __name__ == '__main__':
    main()
