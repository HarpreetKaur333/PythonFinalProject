import math
from math import sqrt

from Quadrilateral import Quadrilateral


class Trapezoid(Quadrilateral):
    def __init__(self, xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4):
        super().__init__(xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4)

    def findHeightOfTrapezoid(self):  # find height
        return self.yPoint3 - self.yPoint4

    def findBase41(self):  # forth side
        return self.xPoint4 - self.xPoint1

    def findBase43(self):  # third side
        return self.xPoint4 - self.xPoint3

    def findBase32(self):  # second side
        return self.xPoint3 - self.xPoint2

    def findBase21(self):  # first side
        return self.xPoint2 - self.xPoint1

    def areaTrapezoid(self):
        return self.findBase32() + self.findBase41()*self.findHeightOfTrapezoid()/2

    def perimeterTrapezoid(self):
        return self.findBase21() + self.findBase41()+self.findBase32()+self.findBase43()
