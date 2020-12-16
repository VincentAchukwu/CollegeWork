import sys
import string
from operator import itemgetter

vowels = "aeiou"

def build_d(s):
   return {l: s.count(l) for l in s if l in vowels}

def main():
    line = sys.stdin.read().lower().strip()
    d = build_d(line)
    words = sorted(d.items(), key=itemgetter(1), reverse=True)
    max_num_width = len(str(max(words, key=len)[1]))
    for vowel, count in words:
       print("{:s} : {:{:d}d}".format(vowel, count, max_num_width))

if __name__ == '__main__':
    main()
