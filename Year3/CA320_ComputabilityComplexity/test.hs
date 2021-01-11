-- useful functions in Haskell

-- first item of list
myHead :: [a] -> a
myHead [] = error "List cannot be empty"
myHead (x:xs) = x

-- last item of list
myLast :: [a] -> a
myLast [] = error "List cannot be empty"
myLast [x] = x
myLast (x:xs) = myLast xs

-- second last item of list
secondLast :: [a] -> a
secondLast xs = last (init xs)

-- tail of list
myTail :: [a] -> [a]
myTail [] = []
myTail (x:xs) = xs

-- everything except last item of list
myInit :: [a] -> [a]
myInit [] = error "List cannot be empty"
myInit [x] = []
myInit (x:xs) = x:(myInit xs)

-- if item present in list
myElem :: (Eq a) => a -> [a] -> Bool
myElem _ [] = False
myElem e (x:xs) = (e == x) || myElem e xs

-- append 2 lists into 1
myAppend :: [a] -> [a] -> [a]
myAppend [] ys = ys
myAppend (x:xs) ys = x:(myAppend xs ys)

-- concats list of lists into 1
myConcat :: [[a]] -> [a]
myConcat [] = []
myConcat (x:xs) = x ++ (myConcat xs)

-- length of list
myLength :: [a] -> Int
myLength [] = 0
myLength (_:xs) = 1 + myLength xs

-- reverse a list
myReverse :: [a] -> [a]
myReverse [] = []
myReverse (x:xs) = (myReverse xs) ++ [x]

-- deletes each occurence of item to delete
myDelete :: (Eq a) => [a] -> a -> [a]
myDelete [] _ = []
myDelete (x:xs) e
    | (e == x) = (myDelete xs e)
    | otherwise = x:(myDelete xs e)

-- summation of list of numbers
mySum :: [Int] -> Int
mySum [] = 0
mySum (x:xs) = x + mySum (xs)

-- product of list of numbers
myProduct :: [Int] -> Int
myProduct [] = 1
myProduct [x] = x
myProduct (x:xs) = x * (myProduct xs)

-- even items of list
myEvens :: [Int] -> [Int]
myEvens [] = []
myEvens (x:xs)
    | even x = (x : myEvens xs)
    | otherwise = myEvens xs

-- replace a for b in list
myReplace :: (Eq a) => a -> a -> [a] -> [a]
myReplace a b [] = []
myReplace a b (x:xs)
    | (a==x) = (b: myReplace a b xs)
    | otherwise = x:(myReplace a b xs)

-- gets union of 2 lists
myUnion :: (Eq a) => [a] -> [a] -> [a]
myUnion xs [] = xs
myUnion xs (y:ys) = if (elem y xs) || (elem y ys)
                    then (myUnion xs ys)
                    else myUnion (myAppend xs [y]) ys

-- gets intersection of 2 lists
myIntersection :: (Eq a) => [a] -> [a] -> [a]
myIntersection [] _ = []
myIntersection (x:xs) ys = if (elem x ys)
                        then x:(myIntersection xs ys)
                        else myIntersection xs ys

-- sums tuples within list
addTuples :: [(Int, Int)] -> [Int]
addTuples xs = [x + y | (x,y) <- xs]

-- aka "nub" (remove duplicates)
removeDupl :: (Eq a) => [a] -> [a]
removeDupl [] = []
removeDupl (x:xs)
    | elem x xs = removeDupl xs
    | otherwise = x : removeDupl xs

-- if list is in ascending order
isAsc :: (Ord a) => [a] -> Bool
isAsc [] = True
isAsc [x] = True
isAsc (x:y:xs) = 
    (x <= y) && isAsc (y:xs)

-- maximum element of list
myMaximum :: (Ord a) => [a] -> a
myMaximum [] = error "Cannot get maximum of empty list"
myMaximum [x] = x
myMaximum (x:xs) = if x > myMaximum(xs) then x else myMaximum xs

-- minimum element of list
myMinimum :: (Ord a) => [a] -> a
myMinimum [] = error "Cannot get maximum of empty list"
myMinimum [x] = x
myMinimum (x:xs) = if x < myMinimum(xs) then x else myMinimum xs

-- duplicates each element of list
myDuplicate :: [a] -> [a]
myDuplicate [] = []
myDuplicate (x:xs) = x:x:myDuplicate xs

-- replicates each element of list n-times
myReplicate :: [a] -> Int -> [a]
myReplicate [] _ = []
myReplicate (x:xs) n = (replicate n x) ++ (myReplicate xs n)

hmm = \x y z -> x + y + z

-- first letter of each string in initials format
initials :: String -> String -> String
initials xs ys = [x] ++ ". " ++ [y] ++ "."
    where (x:_) = xs
          (y:_) = ys

-- removes replicates from sorted list
replRemoveSorted :: (Eq a) => [a] -> [a]
replRemoveSorted [] = []
replRemoveSorted [x] = [x]
replRemoveSorted (x:y:xs)
    | (x==y) = (replRemoveSorted xs)
    | otherwise = x:(replRemoveSorted (y:xs))


-- HCF of two numbers
myGCD :: Int -> Int -> Int
myGCD n 0 = n
myGCD m n = myGCD n (m `mod` n)

-- converts decimal to binary
dectobin :: Int -> String
dectobin 0 = "0"
dectobin 1 = "1"
dectobin d 
   | d `mod` 2 == 0 = (dectobin (d `div` 2)) ++ "0"
   | otherwise      = (dectobin (d `div` 2)) ++ "1"
