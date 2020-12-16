class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return (((other.x - self.x) ** 2) + ((other.y - self.y) ** 2)) ** 0.5

class Shape(object):

    def __init__(self, points):
        self.points = points

    def sides(self):
        return [self.points[i].distance(self.points[i + 1]) if i < (len(self.points) - 1) else self.points[i].distance(self.points[0]) for i in range(len(self.points))]

    def perimeter(self):
        return sum(self.sides())


class Triangle(Shape):

    def area(self):
        s = self.perimeter() / 2
        a, b, c = self.sides()

        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Square(Shape):

    def area(self):
        a, b, _, _ = self.sides()
        return a * b
