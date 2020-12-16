import sys

d = {"0": "zero",
     "1": "one",
     "2": "two",
     "3": "three",
     "4": "four",
     "5": "five",
     "6": "six",
     "7": "seven",
     "8": "eight",
     "9": "nine",
     "10": "ten",
     }

def build_d(s):
    nd = {}
    with open(s, "r") as f:
        for line in f:
            eng, irish = line.strip().split()
            d[eng] = irish
    return d

def main():
    nd = build_d(sys.argv[1])
    for line in sys.stdin:
        nums = line.strip().split()
        s = ""
        t = ""
        for n in nums:
            try:
                s = s + " " + d[n]
            except KeyError:
                s = s + " " + "unknown"
        n2w = s.split()
        for w in n2w:
            try:
                t = t + " " + nd[w]
            except KeyError:
                t = t + " " + "unknown"
        print(t.strip())

if __name__ == '__main__':
    main()
