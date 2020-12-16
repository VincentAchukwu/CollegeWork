# Python 3 program run by passing encrypted file as a command line argument.

import string, collections, time, sys, os

caesar_dir = "../../files/caesar-cipher/"
dict_dir = "../../tests/"

class caesarCypher(object):

    # creating instance variables associated to class
    def __init__(self):

        self.lower_alphabet = string.ascii_lowercase # lower case alphabet
        self.upper_alphabet = string.ascii_uppercase # upper case alphabet
        self.punct = string.punctuation              # punctuation

    # returns first line of encrypted file
    def loadTest(self, caesar_dir):

        # file passed in command line is the file to decrypt
        encrypted_input_path = os.path.join(caesar_dir, sys.argv[1])
        with open(encrypted_input_path, "r") as e:
            test_words = e.read().split('\n')[0].split()    #get first line of encrypted text by splitting newline character

        return test_words

    # load dictionary from tests directory for the keygenerator
    def loadDict(self):

        # creating a dictionary list by reading dictionary text file
        dict_path = os.path.join(dict_dir, "britDict.txt")
        with open(dict_path, "r") as c:
            dictionary = c.read().split()

        return dictionary

    # loads encrypted file
    def load_enc_File(self, caesar_dir):

        encrypted_input_path = os.path.join(caesar_dir, sys.argv[1])
        with open(encrypted_input_path, "r") as e:   # read encrypted file, save it to list
            data = e.read()
            cipher = data.split("\n")

        return cipher


    # decrypt does the opposite of encrypt
    # slightly more modified for use of the class
    def decrypt(self, encrypted_msg, key, dec):

        decrypted = ""
        for i in range(len(encrypted_msg)):
            char = encrypted_msg[i]
            locationUpper = self.upper_alphabet.find(char)  # check if current letter is upper case
            locationLower = self.lower_alphabet.find(char)  # check if current letter is lower case
            #(i.e, char can only be lower or upper, so either locationUpper or locationLower will equal -1)
            if char in self.punct:                          # check if punctuation present, if so, include it in final string and continue to next character
                decrypted+=char
                continue

            if locationUpper != -1:                             # if letter is uppercase
                new_location = (locationUpper - key) % len(self.upper_alphabet)     # opposite of what encrypt would do
                decrypted+=self.upper_alphabet[new_location]    # update decrypted string

            elif locationLower != -1:                           # else if letter is lowercase, do same thing
                new_location = (locationLower - key) % len(self.lower_alphabet)
                decrypted+=self.lower_alphabet[new_location]

        # return decrypted
        dec.append(decrypted)
        # print(decrypted)

    # exactly the same as the decrypt method, except it doesn't take additional list parameter
    def tmpdecrypt(self, encrypted_msg, key):

        decrypted = ""
        for i in range(len(encrypted_msg)):
            char = encrypted_msg[i]
            locationUpper = self.upper_alphabet.find(char)
            locationLower = self.lower_alphabet.find(char)
            if char in self.punct:
                decrypted+=char
                continue

            if locationUpper != -1:
                new_location = (locationUpper - key) % len(self.upper_alphabet)
                decrypted+=self.upper_alphabet[new_location]

            elif locationLower != -1:
                new_location = (locationLower - key) % len(self.lower_alphabet)
                decrypted+=self.lower_alphabet[new_location]

        return decrypted

    # generates key by testing longest word from first line of encrytped text file, and returns that key
    def keygenerator(self):

        dictionary = self.loadDict()

        test_words = self.loadTest(caesar_dir)  # load first line of encrypted text file for testing

        longest = max(test_words, key=len)                  # then testing longest word in that line,
        # since it can easily match with small two letter words, etc, since longest word guarantees key to be found
        # e.g if encrypted word is "ex", decrypting that could match with words in dictionary like ab,op,no,hi, etc.
        # It's faster, instead of checking each word just to get the key...
        # FLAW: if longest word in first line is a name, dictionary doesn't contain names and it would't work (unless I use a separate name dictionary)

        # now testing which key (i, which is iterator in for loop) shifts correct amount to get the word
        for i in range(len(self.lower_alphabet)):           # iterating through length of alphabet
            tmp_decrypted = self.tmpdecrypt(longest, i)     # temporary decrypted word (may or may not be an actual word)
            dec_no_punc = tmp_decrypted.strip(self.punct)   # strip away surrounding punctuation to check if word in dictionary

            # if i (the key) shifts word into an actual word, return it, else we increment i as the next key and loop
            if dec_no_punc.lower() in dictionary:
                return i

    # writes key and decrypted text to caesar-cipher directory
    def save_key_dec(self, dec_lst):

        shift_key = self.keygenerator()
        cipher_alphabet = self.upper_alphabet[shift_key:] + self.upper_alphabet[:shift_key]   # rotates alphabet into ciphered alphabet
        file = sys.argv[1]
        # creating file containing key by string formatting encrypted filename (passed from command line) with "-key.txt" in the string
        with open(os.path.join(caesar_dir, "{}-key.txt".format(file[:-4])), "w") as k:
            key = []
            for letter in range(len(self.upper_alphabet)):
                key.append("{} = {}".format(self.upper_alphabet[letter], cipher_alphabet[letter]))
            k.write("\n".join(key))     # did it this way so there's no newline at the end of file

        # write decrypted text to file in similar fashion
        with open(os.path.join(caesar_dir, "{}-decrypted.txt".format(file[:-4])), "w") as d:
            d.write("\n".join(dec_lst))     # sentences join back together to appear in same structure as encrypted text file (for output elegancy..)


        return "{0}-decrypted.txt and {0}-key.txt written in caesar-cipher directory. Exiting.".format(file[:-4])


def main():

    start = time.perf_counter()
    cc = caesarCypher()                 # create instance of class

    cipher = cc.load_enc_File(caesar_dir)

    key = cc.keygenerator()             # calls method to create key
    if key is None:                     # if encrypted word is invalid/key not found, print small message (did this to handle error)
        print("Key not found. Exiting..")
        sys.exit()                      # instead of it giving large error, just exit program if key not found...
    print("Key = ", key)                # prints the key as a number

    print("################### DECRYPTING ###################")
    dec_lst = []                        # will contain decrypted sentences as items in list

    for sentence in cipher:
        dec = []                        # decrypted words stored in list
        for enc_word in sentence.split():
            cc.decrypt(enc_word, key, dec)
        dec_lst.append(" ".join(dec))   # in the end, making decrypted file be the same output format as the encrypted file text.


    decryption_status = cc.save_key_dec(dec_lst)
    print(decryption_status)            # print message that key and decryption have been written

    finish = time.perf_counter()

    print("Program finished in {} second(s)".format(round(finish-start, 2)))

if __name__ == '__main__':
    main()
