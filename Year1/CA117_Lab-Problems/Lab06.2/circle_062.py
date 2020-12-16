import sys
import math
#formula:sqrt((x2-x1)sqrd+(y2-y1)sqrd)
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)) < r1 + r2

if __name__ == '__main__':
    main()
