num :: (Eq a) => a -> [a] -> Int
num _ [] = 0
num n (x:xs)
    | (n == x) = 1 + (num n xs)
    | otherwise = (num n xs)
