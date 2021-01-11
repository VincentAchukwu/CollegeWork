elemSorted :: (Ord a) => a -> [a] -> Bool
elemSorted _ [] = False
elemSorted n (x:xs)
    | (n < x) = False
    | (n == x) = True
    | otherwise = (elemSorted n xs)
