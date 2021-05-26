from Quadrilateral import Quadrilateral


class Square(Quadrilateral):
    def __init__(self, firstPoint, secondPoint, thirdPoint, fourthPoint, diagonal, SumOfHeightOfTwoTriangle, side1,
                 side2, side3, side4, sidesOfSides):
        self.sidesOfSides = sidesOfSides
        super().__init__(firstPoint, secondPoint, thirdPoint, fourthPoint, diagonal, SumOfHeightOfTwoTriangle, side1,
                         side2,
                         side3, side4)

    def areaSquare(self):
        return self.sidesOfSides * self.sidesOfSides

    def perimeterSquare(self):
        return 4 * self.sidesOfSides
