isSum :: Int -> Int -> Int -> Bool
isSum x y z
    | (y + z) == x = True
    | (x + z) == y = True
    | (x + y) == z = True
    | otherwise = False
