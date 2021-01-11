-- This Haskell script contains some simple and common errors.
-- In exercise 1, you should load it into GHCi and note the 
-- error messages that are reported.  You should correct the 
-- errors one at a time by editing and saving this file, then
-- reloading into GHCi.

import Data.Char(chr,ord)

-- Here is a definition of a function that doesn't do anything very
-- useful, but it does show you how to use a where clause.

f :: Int -> Int -> Int
f x y
    | x > 10     = max x y
    | otherwise  = x - y
    where y = y * y

-- Here is a function to give the next character in the Unicode sequence.

next :: Char -> Char
next c = chr(ord c + 1)

-- Here is an attempt to write a definition of a function that adds one
-- to its argument.

increment :: Int -> Int
increment x = y
    where y = x+1

-- Obviously this definition doesn't make sense!
-- How can x possibly equal x+1?  That would mean 0==1 ...
-- Try increment 3 to see what happens.
