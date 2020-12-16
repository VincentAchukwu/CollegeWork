from math import log10

# (code slightly modified and refactored from online)
class ngram_score(object):

    def __init__(self, ngramfile):

        self.ngrams = {}
        # open ngram file and each line is split into a key and a value, then added to self.ngrams
        with open(ngramfile, "r") as n:     # modified to open file (ngramfile)
            for line in n:
                ngram, count = line.strip().split()
                self.ngrams[ngram] = int(count)

        self.L = len(ngram)   # length of ngram
        self.N = sum(self.ngrams.values())  # get the sum of the values in self.ngrams
        self.floor = log10(0.01 / self.N)   # value by which we reduce the score by if ngram isn't present

        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)    # calculate log per value in self.ngrams

    # score method passes in current decrypted text and gives it a score based on frequency of ngram
    def score(self, tmp_dec_text):

        score = 0
        get_ngrams = self.ngrams    # modified to variable instead of using __getitems__
        for i in range(len(tmp_dec_text) - self.L+1):
            # check if current ngram is in self.ngrams
            curr_ngram = tmp_dec_text[i:i+self.L]   # modified to assign variable name to tmp_dec_text index
            if curr_ngram in self.ngrams:
                score += get_ngrams[curr_ngram]     # if it is, we add it's score
            else:
                score += self.floor     # else we add self.floor

        return score
