-- PDA in the form (Start_State, Accepting_States, Transitions)
type PDA = (Int,[Int],[Transition])
-- describes Transitions from (one state, symbol, and top of stack) to (another state and pushing something to stack)
type Transition = ((Int,String,String),(Int,String))
-- Result is either accepted or rejected
data Result = Accept | Reject
    deriving (Show, Eq)

-- storing stack information
type Stack = String
type Input = String
 
-- defining function to test if PDA accepts/rejects a string
run :: PDA -> String -> Result
run pda input = helperFunc startState pda trans "$" input
                where 
                    trans = getTrans pda startState
                    startState = getStart pda

-- gets transitions list from PDA
getAccept :: PDA -> [Int]
getAccept (_,list,_) = list

-- gets starting state of PDA
getStart :: PDA -> Int
getStart (s,_,_) = s 

-- pushes symbol (String) to stack (Stack)
stackPush :: String -> Stack -> Stack
stackPush _ [] = []
stackPush [] stack = stack
stackPush c stack = c ++ stack

-- pops symbol from the stack
stackPop :: String -> Stack -> Stack
stackPop [] stack = stack
stackPop c (s:stack)
    | c == [s] = stack
    | otherwise = []

-- gets transitions of PDA and current state
getTrans :: PDA -> Int ->[Transition]
getTrans (_, _, []) _ = []
getTrans (_, _, ((state, char, popped), (newState, pushedItem)):trans) currState
    | state == currState = ((state, char, popped), (newState, pushedItem)) : getTrans (0, [0], trans) currState
    | otherwise = getTrans (0, [0], trans) currState

-- helper function for outputting the result given current state, PDA, transitions, and Stack info
helperFunc :: Int -> PDA -> [Transition] -> Stack -> Input -> Result
helperFunc currState pda [] (s:[]) [] 
    | elem currState (getAccept pda)= Accept
    | otherwise = Reject

helperFunc currState pda (((_, char, popped), (newState, pushedItem)):trans) (s:[]) [] 
    | char == "" && ((helperFunc newState pda (getTrans pda newState) (stackPush pushedItem (stackPop popped (s:[]))) []) == Accept ) = Accept
    | otherwise = helperFunc currState pda trans (s:[]) []

helperFunc currState pda _ _ [] = Reject
helperFunc _ _ [] _ _ = Reject
helperFunc _ _ _ [] _ = Reject
helperFunc currState pda (((_, char, popped), (newState, pushedItem)):trans) stack (i:input)
    | ((char == "" ) && ((helperFunc newState pda (getTrans pda newState) (stackPush pushedItem (stackPop popped stack)) (i:input)) == Accept )) = Accept
    | ((char == [i]) && ((helperFunc newState pda (getTrans pda newState) (stackPush pushedItem (stackPop popped stack))   input  ) == Accept )) = Accept
    | otherwise = helperFunc currState pda trans stack (i:input) 

-- Checks if the string given to the PDA is a palindrome
pal = (1, [2], [((1, "a", ""), (1, "a")),
              ((1, "b", "") ,(1, "b")),
              ((1, "a", "") ,(2, "")),
              ((1, "b", "") ,(2, "")),
              ((1, "", "") ,(2, "")),
              ((2, "a", "a") ,(2, "")),
              ((2, "b", "b") ,(2, ""))])

-- run this for testing
testPDA :: Result
testPDA = run pal "abaaba"
