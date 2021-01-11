-- Simulating a PDA (Push Down Automaton) involving Stacks

-- PDA in the form (Start_State, Accepting_States, Transitions)
type PDA = (Int, [Int], [Transition])

-- describes Transitions from (one state, symbol, and top of stack) to (another state and pushing something to stack)
type Transition = ((Int, String, String), (Int, String))
-- (currentState, remainingInput, stackContents)
type Configuration = (Int, String, String)
-- Result is either accepted or rejected
data Result = Accept | Reject
    deriving (Show, Eq)

run :: PDA -> String -> Result
run pda input = let config = ((getStartState pda), input,  "")
    in if (checkAcceptConfig config (getAcceptStates pda))
       then Accept
       else let transitions = findTrans pda config
                newConfigs = applyTrans config transitions
                in if (testAcceptance pda newConfigs) then Accept
                   else run' pda newConfigs -- Starting configuration

run' :: PDA -> [Configuration] -> Result
run' pda configs = if (testAcceptance pda configs)
    then Accept
    else generate pda configs
           
generate :: PDA -> [Configuration] -> Result
generate pda [] = Reject
generate pda configs  = let newAcceptableConfigs = (concat (gen pda configs))
    in run' pda newAcceptableConfigs

gen :: PDA -> [Configuration] -> [[Configuration]]
gen _ [] = []
gen pda (h:t) = let newTrans = findTrans pda h
                    newConfigs = applyTrans h newTrans
                    in newConfigs:gen pda t

testAcceptance :: PDA -> [Configuration] -> Bool
testAcceptance pda [] = False
testAcceptance pda@(_, acceptS, _) (h@(state, input, stack):t)
    | (elem state acceptS && input == "" && stack == "") = True
    | (otherwise) = testAcceptance pda t

applyTrans :: Configuration -> [Transition] -> [Configuration]
applyTrans (_, _, _) [] = []   
applyTrans config@(currs, remainInput, stack) (h@(((_, letter, otherS), (newState, pushLetter))):t)
    | ((take 1 remainInput) == letter && (take 1 otherS /= "") && (pushLetter == "")) = (newState, (drop 1 remainInput), drop 1 stack):applyTrans config t
    | ((take 1 remainInput) == letter) = (newState, (drop 1 remainInput), pushLetter ++ stack):applyTrans config t
    | (otherwise) = (newState, remainInput, pushLetter ++ stack):applyTrans config t

findTrans :: PDA -> Configuration -> [Transition]
findTrans pda@(_, _, []) config = []
findTrans pda@(currS, acceptS, (h:t)) config
    | (getTransState config h) = h:findTrans (currS, acceptS, t) config
    | (otherwise) = findTrans (currS, acceptS, t) config

getTransState :: Configuration -> Transition -> Bool
getTransState (configState, input, currStack) ((state, letter, stackItem), (_, _))
    | (configState == state  && (letter == "" || letter == take 1 input) && (stackItem == take 1 currStack || stackItem == "")) = True
    | (otherwise) = False

getStartState :: PDA -> Int
getStartState (startS, _, _) = startS

getAcceptStates :: PDA -> [Int]
getAcceptStates (_, acceptS, _) = acceptS

checkAcceptConfig :: Configuration -> [Int] -> Bool
checkAcceptConfig (currS, input, stack) acceptS
    | (elem currS acceptS && input == "" && stack == "") = True
    | (otherwise) = False

pal = (1, [2], [((1, "a", ""), (1, "a")),
              ((1, "b", "") ,(1, "b")),
              ((1, "a", "") ,(2, "")),
              ((1, "b", "") ,(2, "")),
              ((1, "", "") ,(2, "")),
              ((2, "a", "a") ,(2, "")),
              ((2, "b", "b") ,(2, ""))])

testrun :: Result
testrun = run pal "abbabaababba"

