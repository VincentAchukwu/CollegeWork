from puzzle8Node import Puzzle8Node

def greedy(start, goal):
    # We will start here, so the list of nodes to do is the start
    start.score = start.heuristic(goal)
    done = False
    num_searches = 0
    next = start
    while not done:
        # Find the next position
        num_searches += 1

        if next == goal:
            done = True
        else:
            # Keep searching.
            # What searching. This is a greedy search. Just try the best child.
            children = next.get_children()
            # Get the score for each of these children
            for child in children:
                child.score = child.heuristic(goal)

            # Best child ...
            best = min(children, key = lambda x : x.score)
            if best.score < next.score:
                next = best # we improved, start from here.
            else:
                done = True # Our move made no progress ... hang our head in shame and give up.

    return num_searches, next

def main():
    
    start = Puzzle8Node("167 82435")
    goal = Puzzle8Node("6183475 2")

    print(greedy(start, goal))

if __name__ == '__main__':
    main()
