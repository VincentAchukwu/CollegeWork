import sys

def main():
    s = list(sys.argv[1])
    for i in range(1, len(s), 2):
        s[i], s[i - 1] = s[i - 1], s[i]
    print("".join(s))

if __name__ == '__main__':
    main()
