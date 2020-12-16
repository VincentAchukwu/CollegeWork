from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry
            # self.table[index].add(item) -
            # return None                 -}to print where collsions are

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
            # return (index, item) >>check where collisons are

    def average_bucket_length(self):
        tot = 0
        count = 0
        for ll in self.table:
            if ll != None:
                tot = len(ll) + tot
                count += 1
        return tot / count

    def min_max_bucket_length(self):
        maxb = 0
        for ll in self.table:
            if ll != None and len(ll) > maxb:
                maxb = len(ll)

        minb = maxb
        for ll in self.table:
            if ll != None and len(ll) < minb:
                minb = len(ll)
        return(minb, maxb)

    def __iter__(self):
        for ll in self.table:
            if ll != None:
                for item in ll:
                    yield item
    def str_hash(s):
        """ Return a normal hash, unless it is a string. """
        if not isinstance(s, str):
            return hash(s) # not a string => use the normal hash function
        else:
            h = 0
            # for i in range(len(s)): h += ord(s[i]) * (31 ** (len(s[i:]) - 1))
            for i in s:
                h += ord(i)  # Get the ASCII value of EACH char of the string as the hash!
            return h
