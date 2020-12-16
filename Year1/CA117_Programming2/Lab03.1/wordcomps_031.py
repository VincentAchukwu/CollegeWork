import sys

def word17(l):
    return [w for w in l if len(w) == 17]

def word18(l):
    return [w for w in l if len(w) >= 18]
def vowel(word):
    return "a" in word.lower() and "e" in word.lower() and "i" in word.lower() and "o" in word.lower() and "u" in word.lower()

def shortestvword(l):
    return min([w for w in l if vowel(w)], key=len)

def fouras(l):
    return [w for w in l if w.lower().count("a") == 4]

def twoqs(l):
    return [w for w in l if w.lower().count("q") >= 2]

def cie(l):
    return [w for w in l if "cie" in w.lower()]

def anagramsangle(l):
    return [w for w in l if sorted(w.lower(), key=str) == sorted("angle", key=str) and w != "angle"]

def iary(l):
    return len([w for w in l if w.lower()[-4:] == "iary"])

def moste(l):
    a = [word.strip() for word in l]
    ecount = [w.lower().count("e") for w in a]
    emax = max(ecount)
    return [w for w in a if w.lower().count("e") == emax]

words = []
def main():
    for line in sys.stdin:
        words.append(line.strip())
    print("Words containing 17 letters:", word17(words))
    print("Words containing 18+ letters:", word18(words))
    print("Shortest word containing all vowels:", shortestvword(words))
    print("Words with 4 a's:", fouras(words))
    print("Words with 2+ q's:", twoqs(words))
    print("Words containing cie:", cie(words))
    print("Anagrams of angle:", anagramsangle(words))
    print("Words ending in iary:", iary(words))
    print("Words with most e's:", moste(words))

if __name__ == '__main__':
    main()
