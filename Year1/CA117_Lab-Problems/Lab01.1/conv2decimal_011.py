import sys

def main():
    lines = sys.stdin
    for line in lines:
        num, base = line.strip().split()
        print(int(num,int(base)))

if __name__ == '__main__':
    main()
