import time, queue, random, threading

class Producer:
    def __init__(self):
        self.product = ["fork", "hammer", "cabbage", "nail"]
        self.next = 0

    def run(self):
        global q
        while time.perf_counter() < 10:
            # print("Queue size: {}".format(q.qsize()))
            if self.next < time.perf_counter():
                f = self.product[random.randrange(len(self.product))]
                g = self.product[random.randrange(len(self.product))]
                q.put(f)
                q.put(g)
                print("Added ting: {}".format(f))
                self.next += random.random()

class Consumer:
    def __init__(self):
        self.next = 0

    def run(self):
        global q
        while time.perf_counter() < 10:
            # print("Queue size: {}".format(q.qsize()))
            if self.next < time.perf_counter() and not q.empty():
                f = q.get()
                print("Added ting: {}".format(f))
                self.next += random.random()
            elif q.empty():
                print("Consumer waiting for product!!!!")

if __name__ == '__main__':
    q = queue.Queue(10)
    p = Producer()
    c = Consumer()

    pt = threading.Thread(target=p.run())
    ct = threading.Thread(target=c.run())

    ct.start()
    pt.start()