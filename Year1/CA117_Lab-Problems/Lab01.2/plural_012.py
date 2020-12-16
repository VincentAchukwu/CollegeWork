import sys

es = ["ch", "sh", "x", "s", "z", "o"]
ves = ["f", "fe"]
vowels = ["a", "e", "i", "o", "u"]

def main():
    for line in sys.stdin:
        word = line.strip()
        if word[-2:] in es  or word[-1:] in es:
            print(word + "es")
        elif word[-2] not in vowels and word[-1] == "y":
            print(word[:-1] + "ies")
        elif word[-2:] in ves or word[-1] in ves:
            print(word.rsplit("f", 1)[0] + "ves")
        else:
            print(word + "s")


if __name__ == '__main__':
    main()
