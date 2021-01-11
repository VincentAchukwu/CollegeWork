def cubes():
    return [num ** 3 for num in range(1,11)]

def wordLen(words):
    return [len(word) for word in words]

def longWordLen(words):
    return [word for word in words if len(word) > 3]

def lettersInWord(word, letter):
    return [char for char in word if char != letter]

def main():
    pass

if __name__ == '__main__':
    main()
