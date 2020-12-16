###############################################################################
############### >> Linked List Class Below << #################################
#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None
        
    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += " " + ptr.item
            ptr = ptr.next
            
        return tmp_str

############ methods ##########################

    def count(self):
        count = 0
        ptr = self.head
        while ptr != None:
            count += 1
            ptr = ptr.next
        return count

    def contains(self, item):
        ptr = self.head
        while ptr != None:
            if ptr.item == item:
                return True
            ptr = ptr.next
        return False

    def after(self, item):
        ptr = self.head
        while ptr != None and ptr.next != None:
            if ptr.next.item == item:
                return ptr.item
            ptr = ptr.next
        return None


    def before(self,item):
        ptr = self.head
        while ptr != None and ptr.next != None:
            if item == ptr.next.item:
                return ptr.item
            ptr = ptr.next
        return None

    def even_count(lst):
        count = 0
        ptr = lst.head
        while ptr != None:
            if not ptr.item % 2:
                count += 1
            ptr = ptr.next
        return count

    def append(self, item):
        if self.empty():
            self.add(item)
        else:
            ptr = self.head
            while ptr != None:
                ptr = ptr.next
            if ptr.next == None:
                ptr.next = Node(item, None)

    def rotate(self):
        return self.append(self.remove())

    def detect_loop(ll):
        item = ll.head
        ptr = ll.head
        while ptr != None and ptr.next != None:
            if ptr.next == item:
                return True
        return False

class Stack:
    def __init__(self):
        self.ll = LinkedList()
    def push(self, item):
        self.ll.add(item)
    def pop(self):
        return self.ll.remove()
    def is_empty(self):
        return self.ll.is_empty()

############ Recursive methods ############
    def recursive_count(self, ptr):
        if ptr == None:
            return 0
        return 1 + self.recursive_count(ptr.next)

    def count(self):
        return self.recursive_count(self.head)

    def evil_count(self, ptr):
        if ptr == None:
            return 0
        return 1 + self.evil_count(ptr.next) if ptr.item % 2 == 0 else self.evil_count(ptr.next)

    def count_even(self):
        return self.evil_count(self.head)

        def is_present(self, item):
        ptr = self.head
        return self.recursive_is_present(ptr, item)

    def recursive_is_present(self, ptr, item):
        if ptr == None:
            return False
        return True if ptr.item == item else self.recursive_is_present(ptr.next, item)

    def largest(self):
        ptr = self.head
        return self.recursive_largest(ptr)

    def recursive_largest(self, ptr):
        if ptr.next == None:
            return ptr.item
        return ptr.item if ptr.item > self.recursive_largest(ptr.next) else self.recursive_largest(ptr.next)

    def duplicates(self):
        ptr = self.head
        return self.recurse_dupl(ptr)
    
    def recurse_dupl(self, ptr):
        if ptr == None or ptr.next == None:
            return False
        return True if ptr.item == ptr.next.item else self.recurse_dupl(ptr.next)
