import sys

def main():
   lines = sys.stdin
   for line in lines:
       line = line.strip().split(".") #first name is line[0]
       i = 0
       while i < len(line[1]) and line[1][i].isalpha():
           i += 1
       print(line[0].capitalize(), line[1][:i].capitalize())

if __name__ == '__main__':
    main()
