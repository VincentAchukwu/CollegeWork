import sys
import string

def main():
    a = []
    count = 0
    for line in sys.stdin:
        words = line.lower().strip().split()
        for word in words:
            a.append(word.strip(string.punctuation))
    for l in set(a):
        if l != "":
            count += 1
    print(count)

if __name__ == '__main__':
    main()
