import sys
from math import pi

def main():
    dp = int(sys.argv[1]) #decimal places (dp)
    print('{:.{}f'.format(pi, dp))

if __name__ == '__main__':
    main()
