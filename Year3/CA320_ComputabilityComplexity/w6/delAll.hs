delAll :: (Eq a) => a -> [a] -> [a]
delAll _ [] = []
delAll n (x:xs)
    | (n == x) = delAll n xs
    | otherwise = x:delAll n xs
