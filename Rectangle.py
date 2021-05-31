import math

from Quadrilateral import Quadrilateral


class Rectangle(Quadrilateral):
    def __init__(self, xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4):
        super().__init__(xPoint1, xPoint2, xPoint3, xPoint4, yPoint1, yPoint2, yPoint3, yPoint4)

    def findDistanceBetweenXCoordinates(self):
        return self.xPoint1 - self.xPoint3
        # return math.sqrt(math.pow(self.xPoint1- self.xPoint3, 2) +
        #                  math.pow(self.yPoint2 - self.yPoint1, 2) * 1.0)

    def findDistanceBetweenYCoordinates(self):
        return self.yPoint2 - self.yPoint3
        # return math.sqrt(math.pow(self.xPoint4 - self.xPoint3, 2) +
        #                  math.pow(self.yPoint4 - self.yPoint3, 2) * 1.0)

    def areaRectangle(self):
        return self.findDistanceBetweenXCoordinates() * self.findDistanceBetweenYCoordinates()

    def perimeterRectangle(self):
        return 2 * self.findDistanceBetweenXCoordinates() + 2 * self.findDistanceBetweenYCoordinates()

    def drawRectangle(self):
        width = int(self.findDistanceBetweenXCoordinates())
        height = int(self.findDistanceBetweenYCoordinates())
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
