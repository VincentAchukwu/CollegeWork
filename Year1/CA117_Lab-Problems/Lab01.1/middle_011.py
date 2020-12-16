import sys

def middle(s):
    return s[len(s) // 2]

def main():
    lines = sys.stdin
    for line in lines:
        if len(line.strip()) % 2 == 1:
            print(middle(line.strip()))
        else:
            print("No middle character!")

if __name__ == '__main__':
    main()
