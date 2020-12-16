import sys

def main():
    count = 0
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
