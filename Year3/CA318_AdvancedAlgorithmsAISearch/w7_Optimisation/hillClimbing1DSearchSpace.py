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
   error = 81 - sol[0] ** 2
   return error ** 2    # Square the error ensures it is always positive.

def main(args):
    if len(args) >= 2:
        num_steps = int(sys.argv[-1])
    else:
        num_steps = 1000

    seed = 43
    random.seed(seed)

    # Wanna get the square root of 81. Easy problem but used here to test the hill climbing algorithm
    # Hill climbing will work in this case because are no local optima.
    # First, assume that the solution is between 1 and 81.
    space = [DimensionRange(1, 81)] # Just one dimension in the range 1 to 81.
    print(space)

    sol = hill_climb(space, cost)
    print("Solution is {}, the cost is {}".format(sol, cost(sol)))

import sys
main(sys.argv)
