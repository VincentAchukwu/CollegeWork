import sys

def sort_on(t):
    return t[1]

def main():
    d = {}
    skips = []
    for line in sys.stdin:
        try:
            name, marks = line.strip().split(":")
            marks_list = marks.split(",")
            mark = sum([int(n) for n in marks_list])
            d[name] = mark
        except ValueError:
            skips.append(name)
            continue
    for k, v in sorted(d.items(), key=sort_on, reverse=True):
        print("{:s} : {:d}".format(k, v))
    print("Skipped:")
    for n in skips:
        print(n)

if __name__ == '__main__':
    main()
