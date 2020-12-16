import sys

with open(sys.argv[1], "r") as f:
    censored = [word.strip() for word in f]

def main():
    for line in sys.stdin:
        word = line.strip()
        for i in censored:
            word = word.replace(i, "@" * len(i))
        print(word)

if __name__ == '__main__':
    main()
