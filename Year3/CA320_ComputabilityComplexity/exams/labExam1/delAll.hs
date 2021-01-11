delAll :: (Eq a) => a -> [a] -> [a]
delAll _ [] = []
delAll e (x:xs)
    | (e == x) = (delAll e xs)
    | otherwise = x:(delAll e xs)
