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

    def findDistance(self):
        dist1 = sqrt((self.xPoint2 - self.xPoint1) ** 2 + (self.yPoint2 - self.yPoint2) ** 2)
        dist2 = sqrt((self.xPoint4 - self.xPoint3) ** 2 + (self.yPoint4 - self.yPoint3) ** 2)

    def areaQuadrilateral(self):
        return 1 / 2 * self.diagonal * self.SumOfHeightOfTwoTriangle

    def perimeterQuadrilateral(self):
        return self.side1 + self.side2 + self.side3 + self.side4
