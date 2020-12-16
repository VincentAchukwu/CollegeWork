import sys

def build_dictionary(filename):
    d = {}
    with open(filename, "r") as f:
        for line in f:
            name, phone, email = line.strip().split()
            d[name] = (phone, email)
    return d

def main():
    nd = build_dictionary(sys.argv[1])
    for line in sys.stdin:
        name = line.strip()
        print("Name: {:s}".format(name))
        if name in nd:
            print("Phone: {:s}".format(nd[name]))
        else:
            print("No such contact")

if __name__ == '__main__':
    main()
