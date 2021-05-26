class Quadrilateral:
    def __init__(self, firstPoint, secondPoint, thirdPoint, fourthPoint, diagonal, SumOfHeightOfTwoTriangle, side1,
                 side2,
                 side3, side4):
        self.side4 = side4
        self.side3 = side3
        self.side1 = side1
        self.side2 = side2

        self.SumOfHeightOfTwoTriangle = SumOfHeightOfTwoTriangle
        self.diagonal = diagonal
        self.fourthPoint = fourthPoint
        self.thirdPoint = thirdPoint
        self.secondPoint = secondPoint
        self.firstPoint = firstPoint

    def areaQuadrilateral(self, ):
        return 1 / 2 * self.diagonal * self.SumOfHeightOfTwoTriangle

    def perimeterQuadrilateral(self):
        return self.side1+self.side2+self.side3+self.side4
