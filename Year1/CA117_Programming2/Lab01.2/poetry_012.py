import sys

def main():
    longest = 0
    lines = []
    for line in sys.stdin:
        words = line.strip()
        lines.append(words)
        if len(words) > longest:
            longest = len(words)
    for l in lines:
        print("{:^{}s}".format(l, longest))

if __name__ == '__main__':
    main()
