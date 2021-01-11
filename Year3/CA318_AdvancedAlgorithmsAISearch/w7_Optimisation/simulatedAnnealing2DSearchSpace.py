import random

import random
import math

def get_small_random_change(current, space, max_step = 1):
    random_index = random.randint(0, len(space)-1)

    # Choose a direction to change it
    random_step = random.randint(1, max_step)
    # Possibly negative
    if random.random() < 0.5:
        random_step = -random_step

    # Create a new list with one of the values changed
    new = current[:]
    new[random_index] += random_step
    if new[random_index] < space[random_index].minimum: # too small? ...
        new[random_index] = space[random_index].minimum # ... fix
    elif new[random_index] > space[random_index].maximum: # too big ...
        new[random_index] = space[random_index].maximum

    return new

def simulated_annealing(space, cost, initial_T = 100.0, final_T = 0.1, cooling_rate = 0.99, max_step = 1):
    # Initialize the values randomly
    current = [random.randint(space[i].minimum, space[i].maximum) for i in range(len(space))]

    for step in range(max_step, 0, -1):
        T = initial_T

        while T > final_T:
            # Choose one of the dimension
            new = get_small_random_change(current, space, step)

            # Is it better ...
            delta = cost(new) - cost(current)
            if delta < 0:
                # ... yep, better, let's take it.
                current = new 
            else:
                # Not better, should we chance it anyway?
                probability = math.e ** (-delta / T) # use the Boltzmann function
                if random.random() < probability:
                    current = new # The man from Boltzmann says yes.

            # Decrease the temperature for the next cycle
            T = T * cooling_rate

    return current

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

    sol = simulated_annealing(space, cost, initial_T = 10.0, final_T = 1.0, cooling_rate = 0.9, max_step = 1)
    print("Solution is {}, the cost is {}".format(sol, cost(sol)))

import sys
main(sys.argv)
