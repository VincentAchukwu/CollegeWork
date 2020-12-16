import sys

def diamond(x):
    i = 1
    while i < x + 1:
        s = (" " * (x - i) + "* " * i).rstrip()
        print(s)
        i += 1
    i = i - 2
    while i > 0:
        s = (" " * (x - i) + "* " * i).rstrip()
        print(s)
        i = i - 1

def main():
    import sys
    n = int(sys.argv[1])
    diamond(n)

if __name__ == '__main__':
    main()
