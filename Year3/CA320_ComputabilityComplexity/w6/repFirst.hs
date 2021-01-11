repFirst :: (Eq a) => a -> a -> [a] -> [a]
repFirst a b [] = []
repFirst a b (x:xs)
    | (a==x) = (b:xs)
    | otherwise = x:(repFirst a b xs)
