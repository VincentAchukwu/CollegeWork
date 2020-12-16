import sys

def main():
    lines = sys.stdin
    for line in lines:
        line = line.lower().strip().split()
        if line[0] in line[1]:
            print(True)
        else:
            print(False)


if __name__ == '__main__':
    main()
