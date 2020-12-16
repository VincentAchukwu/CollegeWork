d = {}

print("Enter a name and number, or a name and ? to query (!! to exit)")

n = input()
while n != "!!":
    user_input = n.strip().split()
    name, query = user_input[0], user_input[1]
    if query != "?":
        d[name] = query
    if (name in d.keys()) and (query == "?"):
        print("{} has number {}".format(name, d[name]))
    elif (name not in d.keys()) and (query == "?"):
        print("Sorry, there is no {}".format(name))
    n = input()
print("Bye")
