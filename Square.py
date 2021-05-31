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
        return math.pow(self.findDistance(), 2)  # length of any side (they are all the same)

    def perimeterSquare(self):
        return 4 * self.findDistance()

    def drawRectangle(self):
        width = int(self.findDistance())
        height = int(self.findDistance())
        print("side of width " + str(width))
        print("side of width " + str(height))
        for i in range(width):
            # self.findDistanceBetweenYCoordinates()
            for j in range(height):
                if i == 0 or i == (width - 1) or j == 0 or j == (height - 1):
                    print("*", end=" ")
                else:
                    print("*", end=" ")
            print("")
