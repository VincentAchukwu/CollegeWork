def longest_common_subsequence(s, t):
    # Create an appropriately sized memo
    memo = [ [-1 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    # Set first row and first column to zero (represents a zero length string => 0 length lcs)
    # Row is s, col is t
    for row in range(len(s)+1):
        memo[row][0] = 0

    for col in range(len(t)+1):
        memo[0][col] = 0
        
    # Do the DP stuff here
    # for loops for s_index and t_index and build up the larger solutions from the smaller solutions.

    for s_index in range(1, len(s) + 1):
        for t_index in range(1, len(t) + 1):

            # ***same method***
            # if s[s_index - 1] == t[t_index - 1]:
            #     memo[s_index][t_index] = memo[s_index - 1][t_index - 1] + 1
            # else:
            #     memo[s_index][t_index] = max(memo[s_index - 1][t_index], memo[s_index][t_index - 1])

            move_both = memo[s_index - 1][t_index - 1] + 1 if s[s_index - 1] == t[t_index - 1] else 0
            move_s = memo[s_index - 1][t_index]
            move_t = memo[s_index][t_index - 1]

            # Return the largest of the three moves
            memo[s_index][t_index] = max([move_both, move_s, move_t])

    # usually return memo[len(s)][len(t)] at this point, but for this exercise
    return memo

def main():
    print(longest_common_subsequence('cat', 'fact'))

if __name__ == '__main__':
    main()
