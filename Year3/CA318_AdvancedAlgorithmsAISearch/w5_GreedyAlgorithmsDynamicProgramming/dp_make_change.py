import math

#   find the smallest number of coins to make up the specified amount
#   using dynamic programming.
#
#   return the memo as result

def dp_make_change(amount, coins):
    assert amount >= 0
    # Initialise memo to be infinity for each of amount + 1 values
    memo = [math.inf] * (amount + 1)

    memo[0] = 0
    for currAmount in range(1, amount + 1):
        memo[currAmount] = min([1 + memo[currAmount - coin] for coin in coins if coin <= amount])
    return memo    

# ***ALTERNATIVE SOLUTION (I think lol)***
# def dp_make_change(amount, coins):
#     assert amount >= 0
#     # Initialise memo to be infinity for each of amount + 1 values
#     memo = [math.inf] * (amount + 1)

#     # Insert code here
#     memo[0] = 0
#     for currAmount in range(1, amount + 1):
#         usedCoinsCount = [0] * len(coins)
#         currTotal = 0
#         j = 0
#         while j < len(coins):
#             if currTotal + coins[j] <= currAmount:
#                 usedCoinsCount[j] += 1
#                 currTotal += coins[j]
#             else:
#                 j += 1
#         memo[currAmount] = sum(usedCoinsCount)

#     return memo

def main():
    print(dp_make_change(12, [5, 2, 1]))

if __name__ == '__main__':
    main()
