import sys

def main():
   lines = sys.stdin
   for line in lines:
       line = line.strip().split()
       lst = [word[:-1] + word[-1].upper() for word in line]
       print(" ".join(lst))

if __name__ == '__main__':
   main()
