data BMI = VSUnderweight | SUnderweight |Underweight | Normal | Overweight | MObese | SObese | VSObese
    deriving (Show, Ord, Eq)

type Person = (Int, Float)

bmiCalculator :: Person -> BMI
bmiCalculator (weight, height)
    | (fromIntegral weight / (height ** 2)) <= 15 = VSUnderweight
    | (fromIntegral weight / (height ** 2)) <= 16 = SUnderweight
    | (fromIntegral weight / (height ** 2)) <= 18.5 = Underweight
    | (fromIntegral weight / (height ** 2)) <= 25 = Normal
    | (fromIntegral weight / (height ** 2)) <= 30 = Overweight
    | (fromIntegral weight / (height ** 2)) <= 35 = MObese
    | (fromIntegral weight / (height ** 2)) <= 40 = SObese
    | otherwise = VSObese

