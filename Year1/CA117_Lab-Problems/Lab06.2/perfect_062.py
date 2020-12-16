import sys

def sumFac(n):
    factors = [i for i in range(1, n // 2 + 1) if not n % i]
    return sum(factors)

def isPerfect(n):
    return n == sumFac(n)

def main():
    nums = [int(line.strip()) for line in sys.stdin]
    for n in nums:
        print(isPerfect(n))

if __name__ == '__main__':
    main()
