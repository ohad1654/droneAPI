from math import sqrt, cos, sin, radians
from Primitives.point import Point


def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


class Line:
    def __init__(self, point1: Point, point2: Point):
        if point1 == point2:
            raise Exception("Points of line must be different")
        if point1.x != point2.x:
            self.point1 = point1 if point1.x < point2.x else point2
            self.point2 = point2 if point1.x < point2.x else point1
        else:
            self.point1 = point1 if point1.y > point2.y else point2
            self.point2 = point2 if point1.y > point2.y else point1

        if point2.x != point1.x:
            self.m = (point2.y - point1.y) / (point2.x - point1.x)
        else:
            self.m = float('inf')

    def length(self):
        return self.point1.distance(self.point2)

    def is_intersect(self, start_point, end_point):

        return ccw(self.point1, start_point, end_point) != ccw(self.point2, start_point, end_point) and \
               ccw(self.point1, self.point2, start_point) != ccw(self.point1, self.point2, end_point)

    def shifted_line(self, shift):
        if self.m != 0:
            return Line(
                Point(self.point1.x + shift / sqrt(1 + self.m ** -2),
                      self.point1.y - shift / (self.m * sqrt(1 + self.m ** -2))),
                Point(self.point2.x + shift / sqrt(1 + self.m ** -2),
                      self.point2.y - shift / (self.m * sqrt(1 + self.m ** -2))))
        else:
            return Line(Point(self.point1.x,
                              self.point1.y + shift),
                        Point(self.point2.x,
                              self.point2.y + shift))

    def extended_line(self, s):
        """
        caculate new line with extened length by s in each side
        :return: the new line
        """
        lineAngle = radians(self.point1.angle(self.point2))
        return Line(self.point1 + Point(cos(lineAngle), sin(lineAngle)) * s,
                    self.point2 - Point(cos(lineAngle), sin(lineAngle)) * s)

    def get_presentation(self, delta=0):
        """
        :return: the function representing the line with artorenglae shift by delta
        """
        # 0<=t<=1
        if self.m != 0:
            return lambda t: Point(
                self.point1.x + t * (self.point2.x - self.point1.x) + delta / sqrt(1 + self.m ** -2),
                self.point1.y + t * (self.point2.y - self.point1.y) - delta / (self.m * sqrt(1 + self.m ** -2)))
        else:
            return lambda t: Point(self.point1.x + t * (self.point2.x - self.point1.x),
                                   self.point1.y + t * (self.point2.y - self.point1.y) + delta)
