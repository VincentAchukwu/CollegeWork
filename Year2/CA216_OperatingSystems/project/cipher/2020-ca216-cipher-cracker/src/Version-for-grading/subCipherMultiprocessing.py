import random, time, string, sys, os, multiprocessing

# decodeAlgo was modified by me. All other methods were written from scratch

output_lst = []     # used for writing decrypted message later
subCipher_dir = "../../files/Substitution Cipher/"  # specifying location of Substitution Cipher directory
core_count = multiprocessing.cpu_count()     # theoretical maximum number of processes we can run at any given moment

class SubCipher(object):

    # creating instance variable of upper and lowercase alphabet
    def __init__(self, q):

        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.q = q

    # load the encyrpted file passed in from the command-line (the path is taken care of by using os.path.join())
    def loadfile(self, subCipher_dir):

        encrypted_input_path = os.path.join(subCipher_dir, sys.argv[1])
        with open(encrypted_input_path, "r") as c:
            cipher = c.read()

        return cipher

    # saving the key and decrypted text files to the Substitution Cipher directory using string formatting
    def save_key_dec(self, output, curr_best_key):

        # specifying path to write the key and decrypted text into Substitution Cipher directory
        file = sys.argv[1]
        with open(os.path.join(subCipher_dir, "{}-decrypted.txt".format(file[:-4])), "w") as d:
            d.write(output)

        with open(os.path.join(subCipher_dir, "{}-key.txt".format(file[:-4])), "w") as k:
            keyList = []
            for letter in range(len(self.upper)):
                keyList.append("{} = {}".format(self.upper[letter], curr_best_key[letter]))
            k.write("\n".join(keyList))

        # let user know that decrypted file and key file are now written to Substitution Cipher directory
        return "{0}-decrypted.txt and {0}-key.txt written in Substitution Cipher directory. Exiting.".format(file[:-4])

    def decipher(self, enc_text, key):

        # using string method maketrans() and translate() to translate key to alphabet instead of using replace()
        conversion = str.maketrans(key.upper() + key.lower(), self.lower + self.upper)
        enc_text = enc_text.translate(conversion)   # then convert each lower/upper to upper/lower

        return enc_text     # deciphered text using the current key

    # using the Hill Climbing algorithm to find appropriate key (code modified from online)
    def decodeAlgo(self, cipher, match):

        curr_best_key = list(self.upper)   # curr_best_key is simply the alphabet
        curr_best_score = -99e9            # curr_best_score is the current best score (which is the worst initially)
        parentscore, parentkey = curr_best_score, curr_best_key[:]   # set parentscore and parentkey to the curr_best_score and curr_best_key for now

        i = 0
        while True:

            # (slight modification here)
            random.shuffle(parentkey)   # shuffle current key
            parentkey = "".join(parentkey)
            deciphered = self.decipher(cipher, parentkey)   # decipher using that key
            parentscore = match.score(deciphered)     # set as current parentscore

            # restructered code so separate method does multiprocessing
            results = self.multiprocess(i, cipher, parentkey, parentscore, match, curr_best_key, curr_best_score)

            parentkey, curr_best_key, curr_best_score, i , output = results[0], results[1], results[2], results[3], results[4]
            # print(output)

            if i > 20:  # program can stop if there are no better scores    (my modification)
                return self.save_key_dec(output, curr_best_key)    # write decrypted text and key to their corresponding files in the Substitution Cipher directory and return message


    def multiprocess(self, i, cipher, parentkey, parentscore, match, curr_best_key, curr_best_score):

        # start multiprocessing
        for _ in range(core_count):
            p = multiprocessing.Process(target=self.test_curr_key, args=(cipher, parentkey, parentscore, match)).start()

        # keep track of best score seen so far
        for _ in range(core_count):
            i += 1
            parentkey, parentscore = self.q.get()   # (my modification)

            # print("{} : {}".format(i, parentscore))   # used this to check current iteration and parentscore
            if parentscore > curr_best_score:
                i = 0
                curr_best_score, curr_best_key = parentscore, parentkey  # if parent has better score than current score (curr_best_score), replace curr_best_score and curr_best_key with it
                # print("\nBest score so far: {}".format(curr_best_score))  # used this to check best score so far, but since we're reseting i, no need to check since its 0
                print("    Best key found so far: {}".format(curr_best_key))
                plain = self.decipher(cipher, curr_best_key)

                # converting all uppercase to lowercase and vice versa (my modification for output)
                output = ""
                for letter in plain:
                    if letter.isupper() and letter.isalpha():
                        output+=letter.lower()
                    elif letter.islower() and letter.isalpha():
                        output+=letter.upper()
                    else:
                        output+=letter
                print("    Decrypted text:\n{}\n".format(output))
                # only add to global list if decrypted text was found with better key
                if output:
                    output_lst.append(output)
            parentkey = list(parentkey)     # (slight modification to assign to variable and convert to list)

        # return keys and score to continue loop
        # output[-1] would be the last version of the decrypted message, which is the actual decrypted message
        return [parentkey, curr_best_key, curr_best_score, i, output_lst[-1]]

    # now we find the best possible key based on the score (Hill Climbing Algorithm)
    def test_curr_key(self, cipher, parentkey, parentscore, match):

        nodeCount = 0
        while nodeCount < 1000:
            letter_1 = random.randint(0, 25)    # get random indexes within the range of the key
            letter_2 = random.randint(0, 25)
            child = list(parentkey)    # create copy of parentkey as the current child key
            child[letter_1], child[letter_2] = child[letter_2], child[letter_1]     # swapping the two characters in the current child (altering the key slightly)
            child = "".join(child)
            deciphered = self.decipher(cipher, child)   # decipher using the current child key
            score = match.score(deciphered)     # give this deciphered text a score
            # if child has better score, replace the parent with it, and reset loop
            if score > parentscore:
                parentscore = score
                parentkey = child    # parent now has child key
                nodeCount = 0
            nodeCount = nodeCount + 1

        # add current parent key and parentscore to the multithreading queue
        self.q.put([parentkey, parentscore])


def main():

    start = time.perf_counter()
    # specifying path to quadgrams.txt in order to read from it
    quadgram_dir = "../../tests/"
    quadgram_path = os.path.join(quadgram_dir, "quadgrams.txt")

    # in order to be able to import ngramscore, I added its location to sys.path
    sys.path.insert(1, "../ngramcode/")
    from ngram_score import ngram_score
    match = ngram_score(quadgram_path) # load our quadgram stats


    q = multiprocessing.Queue()
    ss = SubCipher(q)    # creating instance of SubCipher class and passing queue to it
    cipher = ss.loadfile(subCipher_dir)     # loading cipher text file from Substitution Cipher directory

    print(ss.decodeAlgo(cipher, match))


    finish = time.perf_counter()
    print("Program finished in {} second(s).".format(round(finish-start)))   # output info on total execution time


if __name__ == '__main__':
    main()
