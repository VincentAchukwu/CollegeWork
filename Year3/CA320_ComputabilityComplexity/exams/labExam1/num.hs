num :: (Eq a) => a -> [a] -> Int
num _ [] = 0
num n (x:xs) = if (n == x) then (1 + (num n xs)) else (num n xs)
