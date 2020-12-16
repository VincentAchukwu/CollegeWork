import sys

def main():
    try:
        s = sys.argv[1]
        largest = 0
        with open(s, "r") as f:
            for line in f:
                tokens = line.strip().split()
                name = " ".join(tokens[1:])
                mark = int(tokens[0])
                if mark > largest:
                    largest = mark
                    t = name, largest
        print("Best student: {:s}".format(t[0]))
        print("Best mark: {:d}".format(t[1]))
    except FileNotFoundError:
        print("The file {:s} could not be opened".format(s))


if __name__ == '__main__':
    main()
