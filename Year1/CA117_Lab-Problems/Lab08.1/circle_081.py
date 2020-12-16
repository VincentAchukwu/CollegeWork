class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        return (self.x + other.x) / 2, (self.y + other.y) / 2

    def __str__(self):
        return "({:d}, {:d})".format(self.x, self.y)

class Circle(Point):
    def __init__(self, centre, radius=0):
        self.centre = centre
        self.radius = radius

    def __add__(self, other):
        centre = self.centre.midpoint(other.centre)
        radius = self.radius + other.radius
        return Circle(centre, radius)

    def __str__(self):
        l = []
        l.append("Centre: {}".format(self.centre))
        l.append("Radius: {:d}".format(self.radius))
        return "\n".join(l)
