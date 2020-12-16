class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    # s3 = s1 + s2
    def __add__(self, other):
        goals = self.goals + other.goals
        points = self.points + other.points
        return Score(goals, points)

    # s1 += s2
    def __iadd__(self, other):
        self.goals += other.goals
        self.points += other.points
        return self

    def __sub__(self, other):
        goals = self.goals - other.goals
        points = self.points - other.points
        return Score(goals, points)

    def __isub__(self, other):
        self.goals -= other.goals
        self.points -= other.points
        return self

    def __mul__(self, other):
        goals = self.goals * 2
        points = self.points * 2
        return Score(goals, points)

    def __rmul__(self, other):
        goals = 2 * self.goals
        points = 2 * self.points
        return Score(goals, points)

    def __imul__(self, other):
        self.goals *= 2
        self.points *= 2
        return self

    def __gt__(self, other):
        return ((self.goals * 3) + self.points) > ((other.goals * 3) + other.points)

    def __ge__(self, other):
        return ((self.goals * 3) + self.points) >= ((other.goals * 3) + other.points)

    def __lt__(self, other):
        return ((self.goals * 3) + self.points) < ((other.goals * 3) + other.points)

    def __le__(self, other):
        return ((self.goals * 3) + self.points) <= ((other.goals * 3) + other.points)

    def __eq__(self, other):
        return ((self.goals * 3) + self.points) == ((other.goals * 3) + other.points)

    def __str__(self):
        return "{:d} goal(s) and {:d} point(s)".format(self.goals, self.points)
