import math
from math import sqrt

from Quadrilateral import Quadrilateral


class Parallelogram(Quadrilateral):
    def __init__(self, xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4):
        super().__init__(xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4)

    def findBase(self):
        # return self.xPoint2 - self.xPoint1  # here find base
        return math.sqrt(math.pow(self.xPoint2 - self.xPoint1, 2) +
                         math.pow(self.yPoint2 - self.yPoint1, 2) * 1.0)

    def findHeight(self):  # here find height
        return self.yPoint4 - self.yPoint1

    def areaParallelogram(self):
        return self.findBase() * self.findHeight()

    def perimeterParallelogram(self):
        return 2 * (self.findBase() + self.findHeight())

    def drawParallelogram(self):
        row = int(self.findBase())
        for i in range(row):
            print(" " * (row - i) + " *" * (row + 1))
