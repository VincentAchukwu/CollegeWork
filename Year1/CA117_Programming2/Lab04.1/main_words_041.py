import sys
import string

def main():
    d = {}
    words = []
    for line in sys.stdin:
        for word in line.strip().split():
            words.append(word.lower().strip(string.punctuation))
    for k in words:
        if len(k) > 3 and words.count(k) >= 3:
            d[k] = words.count(k)
    max_word_width = len(max(d.keys(), key=len))
    max_number_width = len(str(max(d.values())))
    for k, v in sorted(d.items()):
       print("{:>{:d}s} : {:{:d}d}".format(k, max_word_width, v, max_number_width))


if __name__ == '__main__':
    main()
