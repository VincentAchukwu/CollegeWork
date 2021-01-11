import random

def hill_climb(space, cost):
    count = 0
    # Create a random start solution
    current_sol = [random.randint(space[i].minimum, space[i].maximum) for i in range(len(space))]
    # Main loop
    while True:
        # Create list of neighbouring solutions
        neighbours = []

        for i in range(len(space)): # for each dimension
            # One away in each direction
            if current_sol[i] > space[i].minimum:
                neighbours.append(current_sol[0:i]+[current_sol[i]-1]+current_sol[i+1:])
            if current_sol[i] < space[i].maximum:
                neighbours.append(current_sol[0:i]+[current_sol[i]+1]+current_sol[i+1:])
            # Let's say there are 3 dimensions, then there could be 6 neighbours (up down for each dir)

        # See what the best solution amongst the neighbours is
        best_neighbour = neighbours[0]
        for neighbour in neighbours[1:]:
            if cost(neighbour) < cost(best_neighbour):
                best_neighbour = neighbour

        if cost(best_neighbour) < cost(current_sol):
            count += 1
            current_sol = best_neighbour
        else:
            # If there's no improvement, then we've reached the top
            break

    print(count)
    return current_sol

class DimensionRange():
   def __init__(self, mini, maxi):
      self.minimum = mini
      self.maximum = maxi

   def __str__(self):
      return "({}, {})".format(self.minimum, self.maximum)

   def __repr__(self):
      return str(self)

def cost(sol):
    x = sol[0]
    y = sol[1]

    error1 = 20 - x - y  # This error will be zero when x+y = 20
    error2 = 362 - x**2 - y ** 2 # this error will be zero when x**2+y**2 = 362

    return error1 ** 2 + error2 ** 2

def main(args):
    if len(args) >= 2:
        num_steps = int(sys.argv[-1])
    else:
        num_steps = 1000

    seed = 43
    random.seed(seed)

    space = [DimensionRange(0, 20), DimensionRange(0, 20)] # Two dimensions

    print(space)

    sol = hill_climb(space, cost)
    print("Solution is {}, the cost is {}".format(sol, cost(sol)))

import sys
main(sys.argv)
