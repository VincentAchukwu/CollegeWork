import sys
import string

def longseq(w):
    for l in w:
        if l in string.ascii_lowercase:
            w = w.replace(l, "0")
    return max(w.split("0"), key=len)

def main():
    words = [line.strip() for line in sys.stdin]
    longwords = [longseq(w) for w in words]
    for word in longwords:
        print(word)

if __name__ == '__main__':
    main()
