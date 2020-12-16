print("Enter numbers (-1 to end): ", end="")

# Do your stuff here
l = []  #list of all numbers which were not seen
seen = []   #"" "" that were seen in l already
num = int(input())
while num != -1:
    if num in l:
        seen.append(num)
    else:
        l.append(num)
    num = int(input())

for n in seen:
    print(str(n) + " ", end="")
print()