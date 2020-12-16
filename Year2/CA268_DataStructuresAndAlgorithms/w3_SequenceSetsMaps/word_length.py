# this sent ence cont ains only four lett errr words

def get_counts_dict(word):
    counts = {}
    words_len = []
    for i in word:
        words_len.append(str(len(i)))
    for w_len in words_len:
        counts[int(w_len)] = int(words_len.count(w_len))
    return counts
