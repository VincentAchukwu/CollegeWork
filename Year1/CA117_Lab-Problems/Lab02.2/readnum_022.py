import sys


def main():
    for line in sys.stdin:
        try:
            line = line.strip()
            print("Thank you for {:d}".format(int(line)))
            return line
        except ValueError:
            print("{} is not a number".format(line))

if __name__ == '__main__':
    main()
