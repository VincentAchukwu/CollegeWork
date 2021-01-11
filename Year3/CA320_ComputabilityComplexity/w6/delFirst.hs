delFirst :: (Eq a) => a -> [a] -> [a]
delFirst _ [] = []
delFirst n (x:xs)
    | (n == x) = xs
    | otherwise = x:delFirst n xs
