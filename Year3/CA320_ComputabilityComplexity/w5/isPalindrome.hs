isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome [] = True
isPalindrome [x] = True
isPalindrome xs = (head xs == last xs) && (isPalindrome ( init(tail xs)))

-- init (tail SOME_LIST) gets the tail first, then init removes the last element
-- e.g LST = [1,2,3,4]
-- tail LST = [2,3,4]
-- init tail LST = [2,3]
