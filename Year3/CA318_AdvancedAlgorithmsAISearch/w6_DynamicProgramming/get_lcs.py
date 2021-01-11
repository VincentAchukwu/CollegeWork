def longest_common_subsequence(s, t, memo):
    lcs = ""

    s_index = len(s)
    t_index = len(t)
    while s_index > 0 and t_index > 0:
        if s[s_index - 1] == t[t_index - 1]:
            s_index -= 1
            t_index -= 1
            lcs = s[s_index] + lcs
        elif memo[s_index - 1][t_index] > memo[s_index][t_index - 1]:
            s_index -= 1
        else:
            t_index -= 1

        # doesn't work
        # currValue = memo[s_index][t_index]
        # if (memo[s_index][t_index - 1]) == currValue:
        #     t_index -= 1
        # elif (memo[s_index - 1][t_index - 1] + 1) == currValue:
        #     lcs = t[t_index - 1] + lcs
        #     s_index -= 1
        #     t_index -= 1

    return lcs

def main():
    memo_1 = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 2]]
    memo_2 = [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 2]]
    print(longest_common_subsequence("cat", "fact", memo_1))
    print(longest_common_subsequence("bd", "abcd", memo_2))

if __name__ == '__main__':
    main()
