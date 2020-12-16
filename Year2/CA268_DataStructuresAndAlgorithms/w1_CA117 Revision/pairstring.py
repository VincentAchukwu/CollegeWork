import sys

s = sys.argv[1]

i = 0
while i < len(s) - 1:
    print(s[i:i + 2])
    i += 1
