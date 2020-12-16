import sys
s = sys.argv[1:]

empty = ""

for i in s:
    empty = empty + ":" + i
print(empty + ":")
