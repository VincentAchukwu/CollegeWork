import threading, time, random, queue

# customer arrival interval in seconds
customerWaitMin = 2
customerWaitMax = 5

# barber cutting interval in seconds
barberCutMin = 4
barberCutMax = 10

mutex = threading.Lock()    # create mutex

class BarberShop(object):

    # for each customer in the customer list in the main method, they enter the barber and are added to waiting room list
    waitingCustomers = []

    # creating instance variables of barber list and number of seats
    def __init__(self, barberList, numSeats):

        self.barberList = barberList
        self.numSeats = numSeats

    def barberStart(self):

        print("Barber Shop is now open!")
        bbThreads = []  # creating list of threads for barbers to join() after they start()
        for barber in self.barberList:
            barberthread = threading.Thread(target=self.barberCut, args=(barber,))
            barberthread.start()
        for bbT in bbThreads:   # joining threads
            bbT.join()

    def barberCut(self, barber):

        while True:
            mutex.acquire()     # customer accesses critical section via acquiring lock

            # only cut hair if there is a line of customer, get the first person from that line/queue
            if len(self.waitingCustomers) > 0:
                nextCust = self.waitingCustomers[0]
                del self.waitingCustomers[0]    # remove that customer from the list of waiting customers
                mutex.release()     # release mutex since customer now getting haircut
                barber.cutHair(nextCust)
            else:
                mutex.release()     # release mutex and barber goes to sleep
                if not barber.available():  # checks if no flags are set/no events are set, then sleep
                    print("{} sleeping...".format(barber.name))
                    barber.sleep()  # barber will sleep until an event occurs
                    print("{} is awake".format(barber.name))    # this happens if an event occurs(i.e customer enters shop, barber wakes up)

    # customer enters barber, checks for seats, sits if seats are available, else leaves
    def enterBarber(self, customer):

        mutex.acquire()
        # customer enters barber, leaves if seats are full, else enters waiting room and wakes up barber
        print("\033[34m{} entered barber shop, looking for seat\033[0m".format(customer.name))

        # check if seats are full
        if len(self.waitingCustomers) == self.numSeats:
            print("\033[31mWaiting room full, {} is now leaving.\033[0m".format(customer.name))
            mutex.release()
        else:
            print("\033[33mThere is room, {} sat down and waiting.\033[0m".format(customer.name))
            self.waitingCustomers.append(customer)
            mutex.release()

            # check which barber is free (i.e doesn't have an event marked as set) and wake them up
            for barber in self.barberList:
                if not barber.available():
                    barber.wakeUp()


# customer class which simply creates customer instance
class Customer(object):

    def __init__(self, name):
        self.name = name

# barber class setting functions of barber(s)
# Note: comments of each event method are from Python documentation with more detail.
class Barber(object):
    
    # Event ()
    barberWorkingEvent = threading.Event() # The internal flag is initially false.

    def __init__(self, name):
        self.name = name

    # checks if an event isSet ()
    def available(self):
        return self.barberWorkingEvent.isSet() # Return true if and only if the internal flag is true.

    # barber wait() for an event to occur
    def sleep(self):
        self.barberWorkingEvent.wait() # Block until the internal flag is true. If the internal flag is true on entry, return immediately. Otherwise, block until another thread calls set() to set the flag to true, or until the optional timeout occurs.

    # barber wakes up and event is set()
    def wakeUp(self):
        self.barberWorkingEvent.set() # Set the internal flag to true. All threads waiting for it to become true are awakened. Threads that call wait() once the flag is true will not block at all.

    # clear () event and cut customers' hair
    def cutHair(self, customer):
        # barber wakes up to cut hair
        self.barberWorkingEvent.clear() # Reset the internal flag to false. Subsequently, threads calling wait() will block until set() is called to set the internal flag to true again.

        # display which barber is cutting which customer
        print("{} cutting {}'s hair now.".format(self.name, customer.name))

        # barber cuts hair for random number of seconds
        hairCutPeriod = random.randint(barberCutMin, barberCutMax)
        time.sleep(hairCutPeriod)

        # print that barber is finished customer's hair
        print("\033[34m{} finished cutting {}.\033[0m".format(self.name, customer.name))


def main():

    start = time.perf_counter()

    # create customers, append to list
    customers = []
    customers.append(Customer('Vinny'))     # last customer
    customers.append(Customer('JJ'))
    customers.append(Customer('Simon'))
    customers.append(Customer('Felix'))
    customers.append(Customer('Niko'))
    customers.append(Customer('Ethan'))
    customers.append(Customer('Jack'))
    customers.append(Customer('Bob'))
    customers.append(Customer('Mark'))
    customers.append(Customer('Gordon'))
    customers.append(Customer('Patrick'))
    customers.append(Customer('Margret'))
    customers.append(Customer('Will'))
    customers.append(Customer('James'))
    customers.append(Customer('Josh'))
    customers.append(Customer('Jimmy'))
    customers.append(Customer('Tom'))
    customers.append(Customer('Homer'))
    customers.append(Customer('Brian'))
    customers.append(Customer('Siggi'))
    customers.append(Customer('Wayne'))
    customers.append(Customer('Chris'))
    customers.append(Customer('Bruce'))
    customers.append(Customer('Alfred'))
    customers.append(Customer('Tony'))
    customers.append(Customer('Clark'))
    customers.append(Customer('Lex'))
    customers.append(Customer('Arthur'))    # first customer


    # creating list of 5 barbers
    barberList = []
    barberList.append(Barber("Barber1"))
    barberList.append(Barber("Barber2"))
    barberList.append(Barber("Barber3"))
    barberList.append(Barber("Barber4"))
    barberList.append(Barber("Barber5"))
    barberShop = BarberShop(barberList, 15)      # 15 = number of chairs in Barber Shop
    barberShop.barberStart()    # Open the Barber shop

    # looping while customers are in list
    while len(customers) > 0:
        nextCust = customers.pop()  # remove current customer from customer list
        barberShop.enterBarber(nextCust)    # customer enters Barber Shop, barber list passed into method
        customerWaitingTime = random.randint(customerWaitMin, customerWaitMax)
        time.sleep(customerWaitingTime)

    finish = time.perf_counter()
    print("Barber Shop closing, Finished in {} seconds.".format(round(finish - start)))

    # keyboard interrupt to exit program..

if __name__ == '__main__':
    main()
