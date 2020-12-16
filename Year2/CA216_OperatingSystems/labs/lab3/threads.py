# from threading import Thread
# import time
# import sys

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)

# def strCount(string, char):
#     return string.count(char)

# def main():
#     start = time.perf_counter()
#     print("This is a thread")
#     lst = []
#     t1 = Thread(target=fact, args=(990,))
#     t1.start()
#     t1.join()
#     # t2 = Thread(target=fact, args=(100,))
#     # t3 = Thread(target=fact, args=(50,))
#     # lst.append(t1)
#     # lst.append(t2)
#     # lst.append(t3)
#     # for t in lst:
#     #     t.start()
#     # for t in lst:
#     #     t.join()
#     # t2 = Thread(target=strCount, args=("hello","c")).start()
#     # t2 = Thread(target=fact, args=(5))
#     # t3 = Thread(target=fact, args=(6))
#     # lst.append(t1)

#     finish = time.perf_counter()
#     print("Finito in {}".format(round(finish - start, 2)))

# if __name__ == '__main__':
#     main()

import time
# from threading import Thread
import concurrent.futures

start = time.perf_counter()

def do_something(delay):
    print("Sleeping {} second(s)...".format(delay))
    time.sleep(delay)
    return "Done Sleeping...{}".format(delay)

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    result = executor.map(do_something, secs)

    # for r in result:
    #     print(r)

# lst = []
# for _ in range(10):
#     t1 = Thread(target=do_something, args=(1.5,))
#     t1.start()
#     lst.append(t1)

# for thread in lst:
#     thread.join()

finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start,2)))
