delOdds :: [Int] -> [Int]
delOdds [] = []
delOdds (x:xs)
    | even x = (x : delOdds xs)
    | otherwise = delOdds xs
