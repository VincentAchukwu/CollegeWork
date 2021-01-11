# if sub is a subsequence of str otherwise False
def is_subsequence(sub, string):

    subIndex = 0
    stringIndex = 0
    # compares current char of str1 with str2
    # if match is found, we check next char of str1
    # regardless, we check next char of str2
    while subIndex < len(sub) and stringIndex < len(string):
        if sub[subIndex] == string[stringIndex]:
            subIndex = subIndex + 1
        stringIndex = stringIndex + 1

    # If all characters of sub matched, then subIndex is equal to length of sub
    return subIndex==len(sub)

def is_common_subsequence(sub, first, second):

    subIndex1 = 0
    firstIndex = 0

    while (subIndex1 < len(sub)) and (firstIndex < len(first)):
        if (sub[subIndex1] == first[firstIndex]):
            subIndex1 += 1
        firstIndex += 1

    subIndex2 = 0
    secondIndex = 0
    while (subIndex2 < len(sub)) and (secondIndex < len(second)):
        if (sub[subIndex2] == second[secondIndex]):
            subIndex2 += 1
        secondIndex += 1

    # If all characters of sub matched, then subIndex is equal to length of sub
    return (subIndex1 == len(sub)) and (subIndex2 == len(sub))


def main():
    print(is_subsequence("cat", "adtc"))
    print(is_subsequence("cat", "caadt"))
    print(is_common_subsequence("cat", "catheat", "topcat"))

if __name__ == '__main__':
    main()
