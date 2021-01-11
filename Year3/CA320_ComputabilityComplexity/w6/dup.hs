dup :: (Eq a) => [a] -> Bool
dup [] = False
dup [x] = False
dup (x:xs)
    | (elem x xs) = True
    | otherwise = (dup xs)
