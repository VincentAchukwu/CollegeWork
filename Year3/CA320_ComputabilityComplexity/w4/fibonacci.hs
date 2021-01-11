fibonacci :: Int -> Int
fibonacci n
    | n == 1    = 0
    | n == 2    = 1
    | otherwise = (fibonacci (n-1) + fibonacci(n-2))

-- n = (0 : 1 : zipWith (+) n (tail n)) gets you infinite fib sequence
