def make_sum_greedy(total, coins):
    usedCoinsCount = [0] * len(coins)
    currTotal = 0
    i = 0
    while i < len(coins):
        if currTotal + coins[i] <= total:
            usedCoinsCount[i] += 1
            currTotal += coins[i]
            i = 0
        else:
            i += 1

    return usedCoinsCount

def minCoins(amount, coins, memo):
    assert amount >= 0

    if amount == 0:
        return 0 # base case

    elif amount in memo:
        return memo[amount]
        # Try every possibility

    else:
        memo[amount] = min([1 + minCoins(amount - coin, coins, memo) for coin in coins if coin <= amount])

    return memo[amount]

# The amount is 23 and the coins are [27, 15, 11, 1]
def main():
    memo = {}
    # print(make_sum_greedy(12, [5, 2, 1]))
    print(minCoins(12, [5, 2, 1], memo))
    # print("Greedy method: {}".format(make_sum_greedy(23, [27, 15, 11, 1])))
    # print("Non-Greed method: {}".format(minCoins(23, [27, 15, 11, 1], memo)))

if __name__ == '__main__':
    main()
