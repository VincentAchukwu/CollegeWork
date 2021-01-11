nubSorted :: (Eq a) => [a] -> [a]
nubSorted [] = []
nubSorted [x] = [x]
nubSorted (x:y:xs)
    | (x==y) = x:(nubSorted xs)
    | otherwise = x:(nubSorted (y:xs))
