import sys

def contains(chars, s):
    for c in chars:
        if c in s:
            s = s.replace(c, "", 1)
        else:
            return False
    return True

def main():
    lines = sys.stdin
    for line in lines:
        line = line.lower().strip().split()
        print(contains(line[0], line[1]))

if __name__ == '__main__':
    main()
