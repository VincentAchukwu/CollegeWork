evalPoly :: Int -> [Int] -> Int
evalPoly x [] = 0
evalPoly y (x:xs) = x + y * (evalPoly y xs)
