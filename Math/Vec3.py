import math

class Vec3(object):

    def __init__(self, other):
        self.x, self.y, self.z = other.x, other.y, other.z

    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vec3(self.x-other.x, self.y-other.y, self.z-other.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        if type(other) == type(self):
            return self.x * other.x + self.y * other.y + self.z * other.z;
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float):
        return self * (1.0 / other)

    def __str__(self):
        return "[ {}, {}, {} ]".format(self.x, self.y, self.z)

    def distance(self, other):
        return (self - other).mag()

    def zero(self):
        self.x, self.y, self.z = 0, 0, 0

    def magSquare(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        magSq = self.x * self.x + self.y * self.y + self.z * self.z
        if magSq > 0.0:
            scalar = 1.0 / math.sqrt(magSq)
            return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)
        return Vec3.ZERO

Vec3.ZERO = Vec3(0, 0, 0)
