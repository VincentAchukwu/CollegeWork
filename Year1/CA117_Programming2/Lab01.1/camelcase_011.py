import sys

def main():
    lines = sys.stdin
    for line in lines:
        line = line.strip().split()
        lst = [word.capitalize() for word in line]
        print(" ".join(lst))

if __name__ == '__main__':
    main()
