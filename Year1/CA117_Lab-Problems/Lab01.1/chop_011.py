import sys

def chop(s):
    return s[1:-1]

def  main():
    line = sys.stdin
    for line in lines:
        cs = contains(line.strip())
        if len(cs) > 0:
           print(cs)

if __name__ == '__main__':
   main()
