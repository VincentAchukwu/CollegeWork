data Day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
    deriving (Enum, Show)

data Month = Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sept | Oct | Nov | Dec
    deriving (Enum, Read)

type Date = (Int, Month, Int)

-- returns whether given year is leap year or not
leap :: Int -> Bool
leap x
    | (mod x 400 == 0) = True
    | (mod x 100 == 0) = False
    | (mod x 4 == 0) = True
    | otherwise = False

-- returns number of days per month from given year
mLengths :: Int -> [Int]
mLengths x = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    where
        february = if leap x == True then 29 else 28

numDays :: Date -> Int
numDays (day, month, year) = 
    day
    + sum (take (fromEnum month) (mLengths year))
    + (year - 1753) * 365 + length [yr | yr <- [1753..year-1], leap yr]

dayOfWeek :: Date -> Day
dayOfWeek date = toEnum (mod ((numDays date) - 1) 7)
