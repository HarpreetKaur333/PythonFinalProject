import math
from math import sqrt

from Quadrilateral import Quadrilateral


class Trapezoid(Quadrilateral):
    def __init__(self, xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4):
        super().__init__(xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4)

    def findDistanceBetweenXCoordinates(self):
        return math.sqrt(math.pow(self.xPoint2 - self.xPoint1, 2) +
                         math.pow(self.yPoint2 - self.yPoint1, 2) * 1.0)

    def findDistanceBetweenYCoordinates(self):
        return math.sqrt(math.pow(self.xPoint4 - self.xPoint3, 2) +
                         math.pow(self.yPoint4 - self.yPoint3, 2) * 1.0)

    def areaTrapezoid(self):
        return self.findDistanceBetweenXCoordinates() * self.findDistanceBetweenYCoordinates()

    def perimeterTrapezoid(self):
        return 2 * (self.findDistanceBetweenXCoordinates() + self.findDistanceBetweenYCoordinates())
