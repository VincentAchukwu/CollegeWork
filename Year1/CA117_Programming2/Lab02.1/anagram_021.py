import sys

def anagram(s, t):
    l = []
    m = []
    for i in s:
         l.append(i)
    for i in t:
        m.append(i)
    return sorted(l) == sorted(m)

def main():
    for line in sys.stdin:
        first, second = line.strip().split()
        print(anagram(first, second))
if __name__ == '__main__':
    main()
