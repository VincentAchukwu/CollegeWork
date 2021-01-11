from puzzle8Node import Puzzle8Node

def bfs(start, goal):
    # We will start here, so the list of nodes to do is the start
    todo = [start]
    visited = []
    num_searches = 0
    while len(todo) > 0:
        next = todo.pop(0) # Get (and remove) first element in the list (using the list as a queue)
        num_searches += 1

        if next == goal:
            return num_searches, next
        else:
            # Keep searching.
            visited.append(next) # Remember that we've been here
            children = list(child for child in next.get_children() if child not in visited and child not in todo)
            todo += children

    return num_searches, None # no route to goal, just return how long it took.

def main():
    # "1238 4765" -> "123 64758"
    start = Puzzle8Node("1238 4765")
    goal = Puzzle8Node("123 64758")

    # print(bfs(start, goal))
    poop, hmm = bfs(start, goal)
    print(hmm.get_path())

if __name__ == '__main__':
    main()
