import sys

def main():
   s = sys.argv[1]
   n = int(sys.argv[2])
   n = n % len(s)
   print(s[-n:] + s[:-n])

if __name__ == '__main__':
   main()
