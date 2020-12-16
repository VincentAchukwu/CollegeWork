import sys

def main():
    words = sys.stdin.readlines()
    wordfive = set()
    p = set()
    r = []
    for word in words:
        if len(word.strip()) >= 5:
            wordfive.add(word.strip())
    for word in wordfive:
        f = word
        word = word.lower()
        word = word[::-1]
        capword = word.capitalize()
        if word in wordfive or capword in wordfive:
            r.append(f)
    print(sorted(r, key=str.lower))

if __name__ == '__main__':
    main()
