from math import sqrt, atan2, degrees


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scale: int):
        return Point(self.x * scale, self.y * scale)

    def __hash__(self):
        return (self.x, self.y).__hash__()

    def __str__(self):
        return "({point.x},{point.y})".format(point=self)

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def angle(self, other):
        return degrees(atan2((self - other).y, (self - other).x))

    def to_tuple(self, nY):
        # self.round()
        return self.x, nY - self.y

    def rounded(self):
        return Point(round(self.x), round(self.y))
