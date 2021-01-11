-- defining a binary tree structure (Empty or node with left and right subtrees)
data BinaryTree a = Empty | Node (BinaryTree a) a (BinaryTree a)
                    deriving (Show, Eq)

-- defining function for a leaf node
leaf x = Node Empty x Empty

-- inserts element to binary tree, returns new binary tree with item added
insert :: (Ord a) => a -> BinaryTree a -> BinaryTree a
insert item Empty = leaf item                               -- base case: if tree empty, insert item as leaf
insert item (Node left value right)
    | item == value = Node left item right                  -- else if item to add is less than current item, insert as node with children
    | item < value = Node (insert item left) value right    -- else if item less than current item, traverse left
    | otherwise = Node left value (insert item right)       -- else traverse right

-- searches for element in tree, returns result as boolean 
search :: (Ord a) => a -> BinaryTree a -> Bool
search item Empty = False                   -- if tree empty, return false
search item (Node left value right)
    | item == value = True                  -- else if item found, return true
    | item < value = (search item left)     -- else if item less than current item, traverse left
    | otherwise = (search item right)       -- else traverse right

-- traverses tree via inorder then returns list
inorder :: BinaryTree a -> [a]
-- if tree empty, return empty list
inorder Empty = []
-- else traverse left and right subtrees, adding item to middle of list each time
inorder (Node left value right) = (inorder left) ++ [value] ++ (inorder right)

-- traverses tree via preorder then returns list
preorder :: BinaryTree a -> [a]
-- if tree empty, return empty list
preorder Empty = []
-- else traverse left and right subtrees, adding item to left of list each time
preorder (Node left value right) = [value] ++ (preorder left) ++ (preorder right)

-- traverses tree via postorder then returns list
postorder :: BinaryTree a -> [a]
-- if tree empty, return empty list
postorder Empty = []
-- else traverse left and right subtrees, adding item to right of list each time
postorder (Node left value right) = (postorder left) ++ (postorder right) ++ [value]

-- sample trees + test cases

-- tree with characters
tree1 = Node (Node (leaf 'a') 'b'
                   (leaf 'c')
             ) 'd'
             (Node (leaf 'e') 'f'
                   (leaf 'g')
             )

-- tree with integers
tree2 = Node (Node (leaf 2) 8
                   (leaf 9)
             ) 10
             (Node (leaf 11) 14
                   (leaf 16)
             )

-- testing search method for both trees
isPresent1 = (search 'a' tree1)
isPresent2 = (search 'p' tree1)

isPresent3 = (search 2 tree2)
isPresent4 = (search 100 tree2)

-- testing insert method for both trees
beforeInorder1 = (inorder tree1)    -- show inorder traversal before insertion
newTree1       = (insert 'q' tree1) -- adds item to tree to give new tree
afterInorder1  = (inorder newTree1) -- show inorder traversal before insertion
-- likewise for tree 2
beforeInorder2 = (inorder tree2)
newTree2       = (insert 20 tree2)
afterInorder2  = (inorder newTree2)

-- testing inorder, preorder, and postorder methods for both trees
inorder1   = (inorder tree1)
preorder1  = (preorder tree1)
postorder1 = (postorder tree1)
-- likewise for tree 2
inorder2   = (inorder tree2)
preorder2  = (preorder tree2)
postorder2 = (postorder tree2)
