from WordGameNode import WordGameNode
from WordGameNode import read_dictionary
import sys

def a_star_search(start, goal):
    todo = [start]
    visited = set()
    num_searches = 0
    while len(todo) > 0:
        next = todo.pop(0) # Get (and remove) first element in the list (using the list as a queue)
        num_searches += 1

        if next == goal:
            return num_searches, next
        else:
            # Keep searching.
            visited.add(next) # Remember that we've been here

            # Add children to the todo list and update the score
            for child in next.get_children():
                if child not in visited and child not in todo:
                    child.score = (child.depth + child.heuristic(goal))  # score = g(n) + h(n)
                    # print(child.depth)
                    todo.append(child)

            # Sort the children by score (lowest better)
            # (removing this makes it work for say carry lorry, but slower)
            todo.sort(key = lambda x : x.score)

    return num_searches, None # no route to goal

def main(args):
    if len(args) == 3:
        start_word = args[1]
        goal_word = args[2]
    else:
        start_word = input("Enter the start word: ")
        goal_word = input("Enter the goal word: ")
    assert len(start_word) == len(goal_word)

    # This reads the dictionary and updates the valid_words global variable for WordGameNode.
    read_dictionary("/etc/dictionaries-common/words", len(start_word))
    # read_dictionary("britDict.txt", len(start_word))
    start = WordGameNode(start_word)
    goal = WordGameNode(goal_word)

    num_searches, end = a_star_search(start, goal) # Perform A* Algorithm with "out of place" heuristic
    print(num_searches)
    if end == None:
        print("There is no path from {0} to {1}".format(start, goal))
    else:
        print(end.get_path())

if __name__ == "__main__":
    main(sys.argv)
