def is_prime(number):
    for element in range(2,number):
        if number % element == 0:
            print(number)
            print("NOT PRIME")
            return False
    print(number)
    print("PRIME")
    return True

x = int(input("enter:"))
is_prime(x)
