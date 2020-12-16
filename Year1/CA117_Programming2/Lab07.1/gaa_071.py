class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def greater_than(self, other):
        return (self.goals * 3 + self.points) > (other.goals * 3 + other.points)

    def less_than(self, other):
        return (self.goals * 3 + self.points) < (other.goals * 3 + other.points)

    def equal_to(self, other):
        return (self.goals * 3 + self.points) == (other.goals * 3 + other.points)
