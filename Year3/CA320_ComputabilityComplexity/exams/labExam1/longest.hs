longest :: [[a]] -> [a]
longest [] = []
longest [x] = x
longest (x:xs) = if (length x) > (length (longest xs)) then x else longest xs
