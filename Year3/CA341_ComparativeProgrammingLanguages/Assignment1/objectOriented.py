# Node class
class Node:
    # a node in a BST can have left and right subtrees
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

# Binary Search Tree class
class BST:
    def __init__(self, info):
        self.root = None
        self.info = info    # pass in phoneBook to class

    # recursively adds item to phoneBook with details
    def recurse_add(self, ptr, item, details):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item, details)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item, details)
        self.info[item] = details   # adding item to dictionary (item mapping to details)
        return ptr
        
    # adds item to correct position on the tree
    def add(self, item, details):
        self.root = self.recurse_add(self.root, item, details)
        return self.root    # return the root of the tree afterwards
            
    # recursive function to get count of nodes in tree (not used)
    def count(self):
        return self.r_count(self.root)

    def r_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.r_count(ptr.left) + self.r_count(ptr.right)

    # returns height of tree (recursive) (not used)
    def height(self):
        return self.r_height(self.root)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    # traversing the tree in order
    def in_order(self):
        a = []
        return self.rec_in_order(self.root, a)
    
    def rec_in_order(self, ptr, a):
        if ptr:
            self.rec_in_order(ptr.left, a)
            # print(ptr.item, end=" ")
            a.append(ptr.item)
            self.rec_in_order(ptr.right, a)

        return a

    # traversing the tree pre order (not used)
    def pre_order(self):
        a = []
        return self.rec_pre_order(self.root, a)
    
    def rec_pre_order(self, ptr, a):
        if ptr:
            # print(ptr.item, end=" ")
            a.append(ptr.item)
            self.rec_pre_order(ptr.left, a)
            self.rec_pre_order(ptr.right, a)

        return a

    # traversing the tree post order (not used)
    def post_order(self):
        a = []
        return self.r_post_order(self.root, a)

    def r_post_order(self, ptr, a):
        if ptr:
            self.r_post_order(ptr.left, a)
            self.r_post_order(ptr.right, a)
            a.append(ptr.item)
        return a

    # function allowing iteration of the tree (supplied inorder traversal for iteration)
    def __iter__(self):
        # can iterate via pre_order, in_order, or post_order
        a = [x for x in self.in_order()]
        yield a

    # same as is_present() method, but returns actual node instead of boolean
    def find(self, item):
        if self.root != None:
            return self.rec_find(self.root, item)
        return None

    def rec_find(self, ptr, item):
        if ptr.item == item:
            return ptr
        elif item < ptr.item and ptr.left != None:
            return self.rec_find(ptr.left, item)
        elif item > ptr.item and ptr.right != None:
            return self.rec_find(ptr.right, item)

    # finds smallest value in tree based on ptr passed in
    def findMin(self, ptr):
        while(ptr.left != None):
            ptr = ptr.left
        return ptr

    # ptr = root of tree. Method deletes value and returns new root
    def delete_val(self, ptr, value):
        if ptr == None:
            # if item not found in tree (None), we return the ptr with this message
            print("{} not found. Deletion failed!".format(value))
            return ptr

        # if value to be deleted less than root, traverse left
        elif value < ptr.item:
            ptr.left = self.delete_val(ptr.left, value)

        # else if value to be deleted greater than root, traverse right
        elif value > ptr.item:
            ptr.right = self.delete_val(ptr.right, value)

        # if the value is the same as ptr's value, we delete this node
        else:
            # Case 1: no children present
            if(ptr.left == None) and (ptr.right == None):
                ptr = None

            # Case 2: one child present
            elif ptr.left == None:
                temp = ptr.right
                ptr = None
                return temp

            elif ptr.right == None:
                temp = ptr.left
                ptr = None
                return temp

            # Case 3: 2 children present
            # need to find the smallest value of right subtree to replace the current node
            else:
                temp = findMin(ptr.right)
                ptr.item = temp.item
                ptr.right = self.delete_val(ptr.right, temp, value)

        return ptr

    # checks if item is present in binary tree by calling recursive function
    def is_present(self, item):
        if self.root == None:
            return False
        return self.rec_present(self.root, item)

    # recusively checks if item in binary tree
    def rec_present(self, ptr, item):
        if ptr.item == item:
            return True
        elif item < ptr.item and ptr.left != None:
            return self.rec_present(ptr.left, item)
        elif item > ptr.item and ptr.right != None:
            return self.rec_present(ptr.right, item)
        else:
            return False

    # same as is_present, except return contact info from tree (not used)
    # (pass in name or number as item)
    def getInfo(self, item):
        if self.root == None:
            return None
        return self.recGetInfo(self.root, item)

    def recGetInfo(self, ptr, item):
        if ptr.item == item:
            return ptr.item, self.info[ptr.item]    # e.g output ("Anakin", [123123123, "4 Hillside House"])
        elif item < ptr.item and ptr.left != None:
            return self.recGetInfo(ptr.left, item)
        elif item > ptr.item and ptr.right != None:
            return self.recGetInfo(ptr.right, item)
        else:
            return "{} not in phone book".format(item)

# checks if contact in infoNames/infoNums, then checks if it's in infoNums/infoNames, respectively
def checkFirstTree(tree1, tree2, dictionary):

    # iterating over items in toBeAdded dictionary
    for k, v in dictionary.items():

        # if k = string, check infoNames (tree2) first (since keys are strings in infoNames)
        # since the key could be either a string (name) or number (int)
        if type(k) == str:
            person = k
            if not tree2.is_present(person):
                print("{} was not in infoNames. Adding...".format(person))
                tree2.add(person, v)
            print(checkOtherTree(tree1, k, v, "infoNums"))  # passing in other tree name for output purposes

        else:   # else we check infoNums first (tree1) (since keys are ints in infoNums)
            personNumber = k
            if not tree1.is_present(personNumber):
                print("{} was not in infoNums. Adding...".format(personNumber))
                tree1.add(personNumber, v)
            print(checkOtherTree(tree2, k, v, "infoNames")) # passing in other tree name for output purposes

    return "Finished checking contacts\n"

# checks the other tree specified from checkFirstTree method
# e.g if contact is not in infoNames, it'll add it there, then check if it's in infoNums (or vice versa)
# this ensures that each entry has one copy and that copy is used in both trees.
def checkOtherTree(tree, key, value, treeType):

    otherKey = value[0]
    # for k, v in tree.info.items():
    if not tree.is_present(otherKey):
        message = "{} ({}) was also not in {}. Adding...\n".format(otherKey, key, treeType)
        tree.add(otherKey, [key, value[-1]])
    else:
        message = "{} ({}) is already present in {}.\n".format(otherKey, key, treeType)

    return message

def main():
    # Read each test case

    # made phone numbers this way as 0 at start doesn't work very well
    # and phone numbers as strings made things awkward for checkFirstTree method

    # mapping of contact number to name and address
    # Russell and Denise not in infoNames
    infoNums = {
            869696969: ["Bob", "70 South Avenue"],
            871122334: ["Joe", "19 High Street"],
            894234546: ["Aaron", "90 Castle Road"],
            899999999: ["Denise", "120 Willow Lane"],
            123123123: ["Anakin", "4 Hillside House"],
            897090909: ["Russell", "59 St.Dixons Lane"]
    }

    # mapping of name to contact number and address
    # Michael and Kenobi not in infoNums
    infoNames = {
            "Bob": [869696969, "70 South Avenue"],
            "Joe": [871122334, "19 High Street"],
            "Aaron": [894234546, "90 Castle Road"],
            "Michael": [859071234, "Slough Avenue"],
            "Kenobi": [873454321, "12 George Road"],
            "Anakin": [123123123, "4 Hillside House"],
    }

    # the contacts below may be present in none, one of, or both of the phoneBooks above
    # contacts which are not present in both trees are added to both (e.g "DCU")
    # contacts which are already present in one of the trees will only be added to the one they're missing from (e.g "Kenobi")
    # contacts which are already present in both trees are not added again (e.g "Anakin")

    # if you wish, you can add in contacts to the dictionary below for testing
    toBeAdded = {
            873454321: ["Kenobi", "12 George Road"],
            "Denise": [899999999, "120 Willow Lane"],
            "DCU": [851232321, "Glasnevin, Dublin 9"],
            "Mick": [180012321, "Ballymun"],
            876789876: ["Jonathan", "19 Meadow Park"],
            480268270: ["UCD", "Dublin 4"],
            123123123: ["Anakin", "4 Hillside House"],
            "Anakin": [123123123, "4 Hillside House"]
    }

    # adding the infoNums and infoNames to separate BSTs
    # (i.e mapping of number to name and address, and mapping of name to number and address, respectively)

    # infoNums
    tree1 = BST(infoNums)
    for num in infoNums:
        node1 = tree1.add(num, infoNums[num])   # node1 will always be topnode of tree1

    # infoNames
    tree2 = BST(infoNames)
    for name in infoNames:
        node2 = tree2.add(name, infoNames[name])  # node2 will always be topnode of tree2

    # for tree1 (infoNums), pass in an integer (phone number)
    # for tree2 (infoNames), pass in a string (name)

    # checks if contact from "toBeAdded" dict is missing, from one of, or both, trees
    # e.g
    print(tree2.is_present("Denise"))   # False initially
    print(tree1.is_present(876789876))  # False initially
    print(checkFirstTree(tree1, tree2, toBeAdded))  # adding missing contacts from "toBeAdded" dictionary
    print("############## Testing some of the missing contacts to see if they were added ##############")
    print(tree2.is_present("Denise"))   # now True since it's added
    print(tree1.is_present(876789876))  # now True since it's added

    print("############## Testing more contacts ##############")
    # to check if new contact is in either tree, add it to "toBeAdded" dictionary, then it'll check both trees again
    # e.g below:
    print(tree2.is_present("Vinny"))    # False (missing in both trees)
    print(tree2.is_present("Russell"))  # False (missing in infoNames)
    print(tree1.is_present(859071234))  # False (missing in infoNums)
    # adding to "toBeAdded" dictionary
    toBeAdded["Vinny"] = [202020202, "123 Finglas Street"]  
    toBeAdded["Russell"] = [897090909, "59 St.Dixons Lane"]
    toBeAdded[859071234] = ["Michael", "Slough Avenue"]
    # previously missing contacts will already be present except "Vinny", "Russell", and 859071234 ("Michael")

    print(checkFirstTree(tree1, tree2, toBeAdded))  # adding new missing contacts from toBeAdded dictionary
    # now these should be true
    print(tree2.is_present("Vinny"))
    print(tree2.is_present("Russell"))
    print(tree1.is_present(859071234))

    print("\nAttempting to delete some contacts")
    # deleting some tree items
    # passes in top node and item to be deleted (node1 from tree1, node2 from tree2)
    tree2.delete_val(node2, "Vinny")
    tree1.delete_val(node1, 123123123)
    tree2.delete_val(node2, "Anakin")
    tree2.delete_val(node2, "Molly")   # not found in tree (cannot delete)
    tree1.delete_val(node1, 111111111) # likewise here

    # deleted contacts should now be missing from their trees
    print("{} present in infoNames: {}".format("Vinny", tree2.is_present("Vinny")))
    print("{} present in infoNums: {}".format(123123123, tree1.is_present(123123123)))
    print("{} present in infoNames: {}".format("Anakin", tree2.is_present("Anakin")))
    print("{} present in infoNames: {}".format("Molly", tree2.is_present("Molly")))
    print("{} present in infoNums: {}".format(111111111, tree1.is_present(111111111)))

if __name__ == "__main__":
    main()
