import sys
import string

def main():
    d = {}
    words = []
    for line in sys.stdin:
        for word in line.strip().split():
            words.append(word.lower().strip(string.punctuation))
    for k in words:
        d[k] = words.count(k)
    for k, v in sorted(d.items()):
        print("{:s} : {:d}".format(k, v))


if __name__ == '__main__':
    main()
