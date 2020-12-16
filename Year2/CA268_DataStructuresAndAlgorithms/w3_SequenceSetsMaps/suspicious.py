import sys

s = sys.argv[1]
d = sys.argv[2]

with open(s, "r") as f:
    student = f.readlines()
    
with open(d, "r") as g:
    delinquents = g.readlines()

match = []

for i in student:
    for j in delinquents:
        if i == j:
            match.append(j.strip())
            
match = sorted(match)
i = 0
while i < len(match):
    print("{:d}. {:s}".format(i+1, match[i]))
    i += 1
