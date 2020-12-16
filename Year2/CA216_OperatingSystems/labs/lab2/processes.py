from multiprocessing import *
from time import sleep
import sys

def sayHi():
	print("Hello from process", current_process().pid)

def sayHi2(n):
	print("Hello {} from process {}".format(n, current_process().pid))

def sayHi3(name):
	print("Hi {} from process {} - pid {}".format(name, current_process().name, current_process().pid))

def sayHi4(lock, name):
	lock.acquire()
	print("Hello {} from process {}".format(name, current_process().pid))
	lock.release()

def procEx():
	print("Hello from process", current_process().pid, "(parent process)")
	otherProc = Process(target=sayHi)
	otherProc.start()

def procEx2():
	print("Hello from process", current_process().pid, "(parent process)")
	p1 = Process(target=sayHi)
	p2 = Process(target=sayHi)
	p3 = Process(target=sayHi)
	p1.start()
	p2.start()
	p3.start()

def manyGreetings():
	print("Hello from process", current_process().pid, "(main process)")
	n = "Vinny"
	p1 = Process(target=sayHi2, args=(sys.argv[1],))	#used sys.argv[1] for testing purposes
	p2 = Process(target=sayHi2, args=(sys.argv[1],))
	p3 = Process(target=sayHi2, args=(sys.argv[1],))	
	p1.start()
	p2.start()
	p3.start()

def manyGreetings2():
	name = input("Enter your name: ")
	numProc = int(input("How many processes? "))
	for i in range(numProc):
		sleep(1)	# just to see processes executing per second
		(Process(target=sayHi2, args=(name,))).start()

def manyGreetings3():
	print("Hello from process {} (main process)".format(current_process().pid))
	personName = input("Name plz: ")
	numProc = int(input("How many numbers? "))
	for i in range(numProc):
		sleep(1)
		Process(target=sayHi3, args=(personName + str(i),), name=str(i)).start()
		# placed str(i) beside name just to see loop inc with name

def manyGreetings4():
	lock1 = Lock()
	print("Hello from process {} (main process)".format(current_process().pid))
	for i in range(10):
		# sleep(1)
		Process(target=sayHi4, args=(lock1, "p"+str(i))).start()

def dig(workerName, holeID, lock):
	lock.acquire()
	print("Hiddy-ho! I'm worker {} and today I have to dig hole {}".format(workerName, holeID))
	lock.release()

def assignDiggers():
	lock = Lock()
	workerName = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J"]
	for holeID in range(len(workerName)):
		Process(target=dig, args=(workerName[holeID], holeID, lock)).start()
		sleep(1) # this seems to make it in order

def main():
	assignDiggers()

if __name__ == '__main__':
	main()


############# My Stuff ###############
# import time
# # from multiprocessing import Process
# import concurrent.futures

# start = time.perf_counter()

# def do_something(delay):
# 	print("Sleeping {} second(s)...".format(delay))
# 	time.sleep(delay)
# 	return "Done Sleeping for {} second(s)...".format(delay)

# def main():
# 	lst = []

# 	with concurrent.futures.ProcessPoolExecutor() as executor:
# 		secs = [5,4,3,2,1]
# 		results = executor.map(do_something, secs)

# 		# for n in results:
# 		# 	print(n)
		


# 	# for _ in range(10):
# 	# 	# p = Process(target=do_something, args=(1.5,))

# 	# 	p.start()
# 	# 	lst.append(p)

# 	# for p in lst:
# 	# 	p.join()

# 	finish = time.perf_counter()

# 	print("Finished in {} second(s)".format(round(finish-start,2)))


# if __name__ == '__main__':
# 	main()
