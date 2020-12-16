def above_average(lst):
    avg = sum(lst) / len(lst)
    return [n for n in lst if n > avg]
