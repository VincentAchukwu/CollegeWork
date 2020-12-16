def sum_to_k(lst, k):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] + lst[j] == k:
                print(lst[i], lst[j])
            j += 1
        i += 1
