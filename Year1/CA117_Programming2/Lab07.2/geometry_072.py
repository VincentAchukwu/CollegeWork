class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return (((other.x - self.x) ** 2) + (other.y - self.y) ** 2) ** 0.5

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

class Segment(Point):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        return (self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2

    def length(self):
        return self.p1.distance(p2)

class Circle(Point):
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def overlaps(self, other):
        return self.radius + other.radius > self.centre.distance(other.centre)
