import sys

def ispal(s):
    w = [c.lower() for c in s if c.isalnum()]
    return w == w[::-1]

def main():
    for line in sys.stdin:
        print(ispal(line.strip()))

if __name__ == '__main__':
    main()
