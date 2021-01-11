dupSorted :: (Eq a) => [a] -> Bool
dupSorted [] = False
dupSorted [x] = False
dupSorted (x:y:xs)
    | (x==y) = True
    | otherwise = (dupSorted (y:xs))
