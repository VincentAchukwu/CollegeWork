import sys

def main():
    try:
        s = sys.argv[1]
        largest = 0
        with open(s, "r") as f:
            for line in f:
                try:
                    tokens = line.strip().split()
                    name = " ".join(tokens[1:])
                    mark = int(tokens[0])
                    if mark > largest:
                        largest = mark
                        t = name
                except ValueError:
                    print("Invalid mark {:s} encountered. Skipping.".format(tokens[0]))
        print("Best student: {:s}".format(t))
        print("Best mark: {:d}".format(largest))
    except FileNotFoundError:
        print("The file {:s} could not be opened".format(s))


if __name__ == '__main__':
    main()
