# returns number of tiles out of place
def hLost(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out how many tiles are out of place
    num_tiles_out_of_place = 0
    for tile in range(len(goal)):
        if start[tile] != goal[tile] and start[tile] != " ":
            num_tiles_out_of_place += 1
    
    return num_tiles_out_of_place

# returns manhattan distance
def h(start, goal):
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"

    # Work out the manhattan distance of each tile from its eventual goal
    manhattan_distance = 0
    for i in range(len(start)):
        if start[i] != " " and start[i] != goal[i]:
            ypos_start, xpos_start = divmod(i,3)
            goalIndex = goal.index(start[i])
            ypos_goal, xpos_goal = divmod(goalIndex,3)
            manhattan_distance += abs(xpos_start - xpos_goal) + abs(ypos_start - ypos_goal)

    return manhattan_distance

def main():
    # print(h(" 12345678", "1238 4756"))
    print(h("1 3824756", "1238 4756"))

if __name__ == '__main__':
    main()
