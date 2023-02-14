from Rotation import Rotation
import math
import copy

class Point:
    def __init__(self, a, b = None):
        if(isinstance(a, Point)):
            self.x = copy.deepcopy(a.x)
            self.y = copy.deepcopy(a.y)

        elif(isinstance(b, Rotation)):
            self.x = a * b.cosine
            self.y = a * b.sine
        else:
            self.x = copy.deepcopy(a)
            self.y = copy.deepcopy(b)

    def __add__(self, rhs):
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return self + (-rhs)

    def __mul__(self, scalar):
        if(isinstance(scalar, Point)):
            return self.x * scalar.x + self.y * scalar.y
        return Point(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq___(self, rhs):
        return self.x == rhs.x and self.y == rhs.Y

    def __ne__(self, rhs):
        return not(self == rhs)

    def distTo(self, rhs):
        return math.sqrt((self.x - rhs.x)**2 + (self.y - rhs.y)**2)

    def angleTo(self, rhs):
        return math.atan2(self.x - rhs.x, self.y - rhs.y)

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def norm(self):
        return Point(self.x / self.mag(), self.y / self.mag())

    def rotateBy(self, rhs):
        return Point(self.x * rhs.cosine - self.y * rhs.sine, self.x * rhs.sine + self.y * rhs.cosine)