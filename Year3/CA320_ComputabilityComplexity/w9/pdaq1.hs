-- PDA in the form (Start_State, Accepting_States, Transitions)
type PDA = (Int,[Int],[Transition])
-- describes Transitions from (one state, symbol, and top of stack) to (another state and pushing something to stack)
type Transition = ((Int, String, String),(Int,String))
-- Configuration in the form (currentState, currentInput, currentStack)
type Configuration = (Int, String, String)
-- result is accepted or rejected
data Result = Accept | Reject
    deriving (Show, Eq)

-- defining function to test if PDA accepts/rejects a string
run :: PDA -> String -> Result
-- if string is empty, reject
run _ "" = Reject
-- else we find the path
run (state,finalState,rules) str = findpath ([(state,str,show (state,finalState,rules))]) (state,finalState,rules)

--if list of configurations is not accepted, PDA transitions are applied to it and try again
findpath :: [Configuration] -> PDA -> Result
findpath [] pda = Reject 
findpath (h:t) (a,b,c)
    | accept (h:t) b == True = Accept
    | otherwise = findpath (nextsteps (h:t) c) (a,b,c) 

-- given list of configurations, check if list includes at
-- least one state allowing for acceptance of the string (includes final states too)
accept:: [Configuration] -> [Int] -> Bool
accept [] _ = False
accept _ [] = False
accept (h:t) finalState
    | accept' h finalState = True
    | otherwise = accept t finalState

-- checking if current configuration is accepted or not
-- (i.e. in final state, nothing left to read, and stack is empty)
accept' :: Configuration -> [Int] -> Bool
accept' config [] = False
accept' (currState, currSymbol, stack) [a]
    | currState == a && currSymbol == "" && stack == "" = True
    | otherwise = False

-- based on values in configuration and transition, apply the given transition to configuration
-- each step correlates to slide 32/43 of the Assignment walkthrough
step :: Configuration -> Transition -> [Configuration]

step (a,b,"") ((d,"",""),(g,""))
    | a == d = [(g,b,"")]
    | otherwise = []

step (a,(b:bs),"") ((d,"",""),(g,h))
    | a == d = [(g,bs,[b])]
    | otherwise = []
step (a,(b:bs),"") ((d,"",f),(g,""))
    | a == d = [(g,(b:bs),f)]
    | otherwise = []   
step (a,(b:bs),"") ((d,"",f),(g,h))
    | a == d = [(g,(b:bs),h)]
    | otherwise = []
step (a,(b:bs),"") ((d,[e],""),(g,""))
    | a == d && b == e = [(g,bs,"")]
    | otherwise = []
step (a,(b:bs),"") ((d,[e],""),(g,h))
    | a == d && b == e = [(g,bs,[b])]
    | otherwise = []
step (a,(b:bs),"") ((d,[e],f),(g,""))
    | a == d && b == e = [(g,bs,"")]
    | otherwise = []
step (a,(b:bs),"") ((d,[e],f),(g,h))
    | a == d && b == e =  []
    | otherwise = []

step (a,b,c) ((d,"",""),(g,""))
    | a == d = [(g,b,c)]
    | otherwise = []

step (a,(b:bs),c) ((d,"",""),(g,h))
    | a == d =  [(g,bs,c)]
    | otherwise = []

step (a,b,(c:cs)) ((d,"",[f]),(g,""))
    | a == d && c == f = [(g,b,cs)]
    | otherwise = []
step (a,b,(c:cs)) ((d,"",[f]),(g,h))
    | a == d && c == f = [(g,b,cs++h)]
    | otherwise = []

step (a,(b:bs),c) ((d,[e],""),(g,""))
    | a == d = [(g,bs,c)]
    | otherwise = []
step (a,(b:bs),c) ((d,[e],""),(g,h))
    | a == d && b == e = [(g,bs,[b]++c)]
    | otherwise = []

step (a,(b:bs),(c:cs)) ((d,[e],[f]),(g,""))
    | a == d && b == e && c == f = [(g,bs,cs)]
    | otherwise = []
step (a,(b:bs),(c:cs)) ((d,[e],[f]),(g,h))
    | a == d && b == e && c == f = [(g,bs,cs++h)]
    | otherwise = []

-- applying ruleset of PDA over one configuration and returning a list of the 
-- resulting configuration
steps :: Configuration -> [Transition] -> [Configuration] 
steps config [] = []
steps (a,b,c) (h:t)
    | b /= "" = step (a,b,c) h ++ steps (a,b,c) t
    | otherwise = []

-- applying entire ruleset over each configuration and return a list of the 
-- resulting configuration
-- nextsteps config [] = []
nextsteps :: [Configuration] -> [Transition] -> [Configuration]
nextsteps [] [] = []
nextsteps [] _ = []
nextsteps _ [] = []
nextsteps (h:t) rules = steps h rules ++ nextsteps t rules

-- Checks if the string given to the PDA is a palindrome
pal = (1, [2], [
                ((1, "a", ""), (1, "a")),
                ((1, "b", "") ,(1, "b")),
                ((1, "a", "") ,(2, "")),
                ((1, "b", "") ,(2, "")),
                ((1, "", "") ,(2, "")),
                ((2, "a", "a") ,(2, "")),
                ((2, "b", "b") ,(2, ""))
                ]
        )

-- run this for testing
testPDA :: Result
testPDA = run pal "abaaba"

