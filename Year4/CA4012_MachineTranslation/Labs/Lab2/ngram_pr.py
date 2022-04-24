#!/usr/bin/python

import sys

if (len(sys.argv) != 4):
    sys.stderr.write("Usage: ngram_pr.py reference.txt system.txt n\n")
    sys.exit(1)

ref_f = sys.argv[1]
system_f = sys.argv[2]
n = int(sys.argv[3])

with open(ref_f) as f1:
    ref = f1.readline()

with open(system_f) as f2:
    system = f2.readline()

# Function to create n-grams from input
# Returns a list of n-grams
def get_ngrams(s, n):

    n_grams  = []
    words = s.split()
    if n == 1:
        return words

    n_grams = [words[i:i+n] for i in range(len(words) - n + 1)]
    return n_grams

# Calculate n-gram precision
def ngram_precision(r, s):
    
    total = len(s)
    count = 0
    for word in s:
        if word in r:
            count += 1
    
    p_score = count / total

    return p_score * 100

# Calculate n-gram recall
def ngram_recall(r, s):
    
    total = len(r)
    count = 0
    for word in r:
        if word in s:
            count += 1

    r_score = count / total

    return r_score * 100

ref_ng = get_ngrams(ref, n)
system_ng = get_ngrams(system, n)
p = ngram_precision(ref_ng, system_ng)
r = ngram_recall(ref_ng, system_ng)

print("Precision: " + str(round(p, 2)) + "%")
print("Recall: " + str(round(r, 2)) + "%")
