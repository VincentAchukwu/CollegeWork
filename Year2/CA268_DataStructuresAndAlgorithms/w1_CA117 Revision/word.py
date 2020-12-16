def get_plural(s):
    es = ["ch", "sh", "x", "s", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    sec = s[-2:]
    first = s[-1]
    wordOne = s[:-2]
    wordTwo = s[:-1]
    if sec in es:
        return s + "es"
    elif first in es or first == "o":
        return s + "es"
    elif s[-2] not in vowels and first == "y":
        return wordTwo + "ies"
    elif first == "f":
        return wordTwo + "ves"
    elif sec == "fe":
        return wordOne + "ves"
    else:
        return s + "s"
