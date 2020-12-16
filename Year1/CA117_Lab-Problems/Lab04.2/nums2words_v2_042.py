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

def main():
    for line in sys.stdin:
        nums = line.strip().split()
        s = ""
        for n in nums:
        try:
              s = s + " " + d[n]
        except KeyError:
              s = s + " " + "unknown"
        print(s.strip())

if __name__ == '__main__':
    main()
