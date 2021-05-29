import math
from math import sqrt

from Quadrilateral import Quadrilateral


class Square(Quadrilateral):
    def __init__(self, xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4):
        super().__init__(xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4)

    def findDistance(self):
        return math.sqrt(math.pow(self.xPoint2 - self.xPoint1, 2) +
                         math.pow(self.yPoint2 - self.yPoint1, 2) * 1.0)

    def areaSquare(self):
        return math.sqrt(self.findDistance())  # length of any side (they are all the same)

    def perimeterSquare(self):
        return 4 * self.findDistance()
