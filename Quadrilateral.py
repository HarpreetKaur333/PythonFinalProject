import math
from cmath import sqrt


class Quadrilateral:
    def __init__(self, xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4):
        self.yPoint4 = yPoint4
        self.yPoint3 = yPoint3
        self.yPoint2 = yPoint2
        self.yPoint1 = yPoint1
        self.xPoint4 = xPoint4
        self.xPoint3 = xPoint3
        self.xPoint2 = xPoint2
        self.xPoint1 = xPoint1

    def findDistance1(self):
        return math.sqrt(math.pow(self.xPoint2 - self.xPoint1, 2) +
                         math.pow(self.yPoint2 - self.yPoint1, 2) * 1.0)

    def findDistance2(self):
        return math.sqrt(math.pow(self.xPoint4 - self.xPoint3, 2) +
                         math.pow(self.yPoint4 - self.yPoint3, 2) * 1.0)

    def findDistance3(self):
        return math.sqrt(math.pow(self.xPoint4 - self.xPoint1, 2) +
                         math.pow(self.yPoint4 - self.yPoint1, 2) * 1.0)

    def findDistance4(self):
        return math.sqrt(math.pow(self.xPoint3 - self.xPoint2, 2) +
                         math.pow(self.yPoint3 - self.yPoint1, 2) * 1.0)

    def findS(self):
        return (self.findDistance1() + self.findDistance2() + self.findDistance3() + self.findDistance4()) / 2

    def areaQuadrilateral(self):
        return math.sqrt((self.findS() - self.findDistance1()) *
                         (self.findS() - self.findDistance2()) *
                         (self.findS() - self.findDistance3()) *
                         (self.findS() - self.findDistance4()))

    def perimeterQuadrilateral(self):
        return self.findDistance1() + self.findDistance2() + self.findDistance3() + self.findDistance4()
