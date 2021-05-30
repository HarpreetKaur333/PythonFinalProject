import math
from math import sqrt

from Quadrilateral import Quadrilateral


class Parallelogram(Quadrilateral):
    def __init__(self, xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4):
        super().__init__(xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4)

    def findDistanceBetweenXCoordinates(self):
        return self.xPoint2 - self.xPoint1  # here find base

    def findDistanceBetweenYCoordinates(self):  # here find height
        return self.xPoint2 - self.xPoint4

    def areaParallelogram(self):
        return self.findDistanceBetweenXCoordinates() * self.findDistanceBetweenYCoordinates()

    def perimeterParallelogram(self):
        return 2 * (self.findDistanceBetweenXCoordinates() + self.findDistanceBetweenYCoordinates())
