import sys

def capitals(s):
    return s[0].upper() + s[1:-1] + s[-1].upper()

def main():
   lines = sys.stdin
   for line in lines:
       if len(line.strip()) >= 2:
            cs = capitals(line.strip())
            print(cs)

if __name__ == '__main__':
    main()
