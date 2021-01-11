import Data.Char(toUpper)

stringToUpper :: String -> String
stringToUpper [] = []
stringToUpper (x:xs) = (toUpper x):(stringToUpper xs)
