class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)


############## methods ####################
            
    def count(self):
        return self.r_count(self.root)

    def r_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.r_count(ptr.left) + self.r_count(ptr.right)

    def range_count(self, lo, hi):
        if self.root == None:
            return 0
        return self.rec_range_count(self.root, lo, hi)

    def rec_range_count(self, ptr, lo, hi):
        if ptr == None:
            return 0
        elif ptr.item == lo and ptr.item == hi:
            return 1
        elif lo <= ptr.item <= hi:
            1 + self.rec_range_count(ptr.left,lo,hi) + self.rec_range_count(ptr.right,lo,hi)
        elif ptr.item < lo:
            return self.rec_range_count(ptr.right,lo,hi)
        else:
            return self.rec_range_count(ptr.left,lo,hi)

    def height(self):
        return self.r_height(self.root)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    # def height(self):
    #     if self.root == None:
    #         return 0
    #     return self.rec_height(self.root, 0)

    # def rec_height(self, ptr, curr_height):
    #     if ptr == None:
    #         return 0
    #     left = self.rec_height(ptr.left, curr_height + 1)
    #     right = self.rec_height(ptr.right, curr_height + 1)
    #     return max(left, right)

    def in_order(self):
        return self.rec_in_order(self.root,nl=True)
    
    def rec_in_order(self, ptr,nl):
        if ptr:
            self.rec_in_order(ptr.left,False)
            print(ptr.item, end=" ")
            self.rec_in_order(ptr.right,False)
        if nl:
            print() # print new line in output

    def pre_order(self):
        return self.rec_pre_order(self.root, nl=True)
    
    def rec_pre_order(self, ptr, nl):
        if ptr:
            print(ptr.item, end=" ")
            self.rec_pre_order(ptr.left, nl=False)
            self.rec_pre_order(ptr.right, nl=False)
        if nl:
            print()

    def post_order(self):
        a = []
        return self.r_post_order(self.root, a)

    def r_post_order(self, ptr, a):
        if ptr:
            self.r_post_order(ptr.left, a)
            self.r_post_order(ptr.right, a)
            a.append(ptr.item)
        return a

    def __iter__(self):
        a = [str(x) for x in self.post_order()]
        yield "Print the stuff in post order: \n" + " ".join(a) + " "

    def rotation_type(bst):
        rot_type = ""
        ptr = bst.root
        while ptr != None:
            if ptr.left == None and ptr.right == None:
                return rot_type
            elif ptr.left == None:
                rot_type += "r"
                ptr = ptr.right
            else:
                rot_type += "l"
                ptr = ptr.left
        return rot_type[:len(rot_type)] #excludes last node since it adds extra node in string

    def total(self):
        return self.rec_sum(self.root)

    def rec_sum(self, ptr):
        if ptr == None:
            return 0
        return ptr.item + self.rec_sum(ptr.left) + self.rec_sum(ptr.right)

    def is_present(self, item):
        if self.root == None:
            return False
        return self.rec_present(self.root, item)

    def rec_present(self, ptr, item):
        if ptr.item == item:
            return True
        elif item < ptr.item and ptr.left != None:
            return self.rec_present(ptr.left, item)
        elif item > ptr.item and ptr.right != None:
            return self.rec_present(ptr.right, item)
        else:
            return False

    def count_leaves(self):
        if self.root == None:
            return 0
        return self.rec_leaf(self.root, 1)

    def rec_leaf(self, ptr, count):
        if ptr == None:
            return 0
        elif ptr.left == None and ptr.right == None:
            return 1
        left = self.rec_leaf(ptr.left, count + 1)
        right = self.rec_leaf(ptr.right, count + 1)
        return left + right

    def make_list(lst):
        if len(lst) <= 2:
            return lst
        lst = sorted(lst)
        mid = len(lst) // 2
        root = lst[mid]
        left = make_list(lst[:mid])
        right = make_list(lst[mid + 1:])
        return [root] + left + right

    def maximus(bst):
        return (2 ** (bst.height()) - 1) == (int(bst.count()))

    
def is_avl(bst):
    if bst.root == None:
        return
    return True if abs(bst.r_height(bst.root.left) - bst.r_height(bst.root.right)) <= 1 else False

def main():
    # Read each test case
    nums = [10,20,30,40,50,60,70,80,90]


    tree = BST()
    for num in nums:
        tree.add(num)

    for x in tree:
        print(x)

if __name__ == "__main__":
    main()