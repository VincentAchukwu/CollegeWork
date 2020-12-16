from Queue import Queue

def split(q):
    p = q.__len__() // 2 #10
    S1 = Queue()
    S2 = Queue()
    for i in range(0,p):
        S1.enqueue(q.dequeue())
    while not q.isempty():
        S2.enqueue(q.dequeue())
    return S1,S2

def merge(q1, q2, q):
    """ this function will merge q1 and q2 into q.
        Assuming that q1 and q2 are sorted, this function will
        return q such that q contains the combined elements of q1 and q2 and
        q will also be sorted.
        
        The function returns nothing. The result will be contained in the queue parameter.
    """
    while not q1.isempty() and not q2.isempty():
        if q1.first() < q2.first():
            q.enqueue(q1.dequeue())
        else:
            q.enqueue(q2.dequeue())
    # ensure both queues are fully empty and enqueue to main queue
    while not q1.isempty():
        q.enqueue(q1.dequeue())
    while not q2.isempty():
        q.enqueue(q2.dequeue())