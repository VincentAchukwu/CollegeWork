count = 0
def fib(n, argument):
    global count
    if n == 0 or n == 1:
        return 1
    if n == argument:
        #c[n] += 1
        count += 1
    return fib(n-1, argument) + fib(n-2, argument)

def main():
    # e.g fib(20) with arg 2, fib(2) is called 4181 times
    N = 15
    argument = 4
    print(fib(N, argument))
    print(count)

if __name__ == '__main__':
    main()
