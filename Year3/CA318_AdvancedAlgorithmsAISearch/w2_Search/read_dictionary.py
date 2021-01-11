def read_dictionary(filename, length):

    # your code here
    with open(filename, "r") as f:
        lines = f.readlines()

    # gets words of equal given length, lowercase, and don't have punctuation
    validWords = [word.strip() for word in lines if word.strip().islower() and len(word.strip()) == length and word.strip().isalpha()]

    return validWords # a list of the words in the dictionary which comprise only lower case letters and are of the correct length
