triangleArea :: Float -> Float -> Float -> Float
triangleArea sideA sideB sideC = if ( ((sideA+sideB)>sideC) && ((sideA+sideC)>sideB) && ((sideB+sideC)>sideA) ) == True
    then let s = (sideA + sideB + sideC) / 2 in sqrt(s * (s-sideA ) * (s-sideB) * (s-sideC))
    else error "Not a triangle!"
