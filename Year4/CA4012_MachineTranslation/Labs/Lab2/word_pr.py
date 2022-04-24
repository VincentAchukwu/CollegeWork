#!/usr/bin/python

import sys

if (len(sys.argv) != 3):
    sys.stderr.write("Usage: word_pr.py reference.txt system.txt\n")
    sys.exit(1)

ref_f = sys.argv[1]
system_f = sys.argv[2]

# Read reference sentence from file
with open(ref_f) as f1:
    ref = f1.readline()

# Read system translated sentence from file
with open(system_f) as f2:
    system = f2.readline()

# Function that calculates the word PRECISION and returns it as a percentage
# precision = N(matches in Translation Output) / N(words in Translation Output)
def w_precision(r, s):

    total = len(s.split())
    count = 0
    refList = r.split()
    sysList = s.split()
    for word in sysList:
        if word in refList:
            count += 1
    
    p_score = count / total

    return p_score * 100

# Function that calculates the word RECALL and returns it as a percentage
# precision = N(matches in Reference Output) / N(words in Reference Output)
def w_recall(r, s):

    total = len(r.split())
    count = 0
    refList = r.split()
    sysList = s.split()
    for word in refList:
        if word in sysList:
            count += 1

    r_score = count / total

    return r_score * 100

p = w_precision(ref, system)
r = w_recall(ref, system)

print("Precision: " + str(p) + "%")
print("Recall: " + str(r) + "%")
