from threading import Thread
from time import sleep

def fmap(out, a, b):
    out.append(a * b)

def threading(pairs):
    out = []
    for (a, b) in pairs:
        thread = Thread(target=fmap, args=(out, a, b))
        thread.start()
        thread.join()
    return out

def make_pairs(a):
    if len(a) % 2 != 0:
        a.append(1)
    pairs = []
    for i in range(0, len(a), 2):
        pairs.append((a[i], a[i+1]))
    return pairs

def factorial(N):

    pairs = make_pairs([x for x in range(1, N + 1)])

    while len(pairs) != 1:
        out = threading(pairs)
        while len(out) != len(pairs):
            sleep(0.01)

        pairs = make_pairs(out)
        print(pairs)

    return pairs[0][0] * pairs[0][1]

if __name__ == '__main__':
    print(factorial(10))
