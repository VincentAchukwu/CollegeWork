-- defining a binary tree structure (Empty or node with left and right subtrees)
data Tree a = Null | Node a (Tree a) (Tree a)
                deriving (Read, Show)

-- defining function for a leaf node
leaf x = Node x Null Null

addNode :: (Ord a) => a -> Tree a -> Tree a
addNode item Null = leaf item                               -- base case: if tree empty, insert item as leaf
addNode item (Node value left right)
    | item == value = Node item left right                   -- else if item to add is less than current item, insert as node with children
    | item < value = Node value (addNode item left) right    -- else if item less than current item, traverse left
    | otherwise = Node value left (addNode item right)       -- else traverse right

makeTree :: (Ord a) => [a] -> Tree a
makeTree [] = Null
makeTree [x] = leaf x
makeTree (x:xs) = addNode x (makeTree xs)

inOrder :: Tree a -> [a]
inOrder Null = []
inOrder (Node item left right) = (inOrder left) ++ [item] ++ (inOrder right)

mpSort :: (Ord a) => [a] -> [a]
mpSort items = inOrder (makeTree items)

-- extra functions I added from David Sinclair's lab
hoAddNode :: (Ord a) => (a -> a -> Bool) -> a -> Tree a -> Tree a
hoAddNode _ item Null = leaf item
hoAddNode f item (Node value left right)
    | item `f` value = Node value (hoAddNode f item left) right
    | otherwise = Node value left (hoAddNode f item right)

hoMakeTree :: (Ord a) => (a -> a -> Bool) -> [a] -> Tree a
hoMakeTree _ [] = Null
hoMakeTree _ [x] = leaf x
hoMakeTree f (x:xs) = hoAddNode f x (hoMakeTree f xs)

hoSort :: (Ord a) => (a -> a -> Bool) -> [a] -> [a]
hoSort f lst = inOrder (hoMakeTree f lst)

-- example tree:
tree1 = Node 'd' (Node 'b' (leaf 'a')
                   (leaf 'c')
             )
             (Node 'f' (leaf 'e')
                   (leaf 'g')
             )
