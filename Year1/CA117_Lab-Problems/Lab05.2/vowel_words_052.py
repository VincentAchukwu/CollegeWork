import sys

vowels = "aeiou"

def main():
    for line in sys.stdin:
        word = line.strip()
        for l in word:
            if l.lower() not in vowels:
                word = word.replace(l, "").lower()
        if word == vowels:
            print(line.strip())

if __name__ == '__main__':
    main()
