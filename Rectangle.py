from Quadrilateral import Quadrilateral


class Rectangle(Quadrilateral):
    def __init__(self, firstPoint, secondPoint, thirdPoint, fourthPoint, diagonal, SumOfHeightOfTwoTriangle, side1,
                 side2, side3, side4, rLength, rWidth):
        super().__init__(firstPoint, secondPoint, thirdPoint, fourthPoint, diagonal, SumOfHeightOfTwoTriangle, side1,
                         side2,
                         side3, side4)
        self.rWidth = rWidth
        self.rLength = rLength

    def areaRectangle(self):
        return self.rLength * self.rWidth

    def perimeterRectangle(self):
        return 2 * self.rLength + 2*self.rWidth
