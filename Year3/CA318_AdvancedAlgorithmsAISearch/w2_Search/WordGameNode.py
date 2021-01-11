from string import ascii_lowercase
# from read_dictionary import read_dictionary

# faster to use set since it has O(1) time complexity search (if it contains word)
valid_words = set()

class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __str__(self):
        return self.name
        #return "N({0}, {1})".format(self.name, self.children)

    def __repr__(self):
        return str(self)

    def get_children(self):
        return self.children

    # See https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.name == other.name
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))

# valid_words = None

def read_dictionary(filename, length):

    # your code here
    global valid_words
    valid_words = set()
    length = int(length)
    with open(filename, "r") as f:
        lines = f.readlines()

    # words = [word.strip() for word in lines if (word.strip().islower()) and (len(word.strip()) == length)]
    # gets words of equal given length, lowercase, and don't have punctuation
    valid_words = {word.strip() for word in lines if word.strip().islower() and len(word.strip()) == length and word.strip().isalpha()}

    # return valid_words # words in the dictionary which comprise only lower case letters and are of the correct length


class WordGameNode(Node):
    def __init__(self, name, parent = None):
        # Ensure lowercase letters (no digits or special chars)
        for letter in name:
            assert letter in ascii_lowercase

        # global valid_words
        # if valid_words == None or len(valid_words) != len(name):
            # We only need to examine words which have the same length as our word (self.name)
            # valid_words = read_dictionary("/etc/dictionaries-common/words", len(name))
            # valid_words = read_dictionary("britDict.txt", len(name))
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name

    def get_children(self):
        lower = ascii_lowercase
        global valid_words
        child_words = []
        for i in range(len(self.name)):
            child_words += [WordGameNode("{}".format(self.name[:i] + letter + self.name[i + 1:]), self) for letter in lower if ((self.name[:i] + letter + self.name[i + 1:]) != self.name) and ((self.name[:i] + letter + self.name[i + 1:]) in valid_words)]

        return child_words

    def get_path(self):
        # insert code here
        path = [self]
        while self.parent is not None:
            print(path)
            path.append(self.parent)
            self = self.parent
        return path
