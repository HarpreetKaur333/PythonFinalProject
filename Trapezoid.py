from Quadrilateral import Quadrilateral


class Trapezoid(Quadrilateral):
    def __init__(self, firstPoint, secondPoint, thirdPoint, fourthPoint, bases, Height, legsHeight1, legsHeight2,
                 legsHeight3, legsHeight4):
        self.legsHeight4 = legsHeight4
        self.legsHeight3 = legsHeight3
        self.legsHeight2 = legsHeight2
        self.legsHeight1 = legsHeight1
        self.Height = Height
        self.bases = bases
        self.fourthPoint = fourthPoint
        self.thirdPoint = thirdPoint
        self.secondPoint = secondPoint
        self.firstPoint = firstPoint
        super().__init__(firstPoint, secondPoint, thirdPoint, fourthPoint)

    def areaQuadrilateral(self):
        return self.bases + self.bases / 2 * self.Height

    def perimeterQuadrilateral(self):
        return self.legsHeight1 + self.legsHeight2 + self.legsHeight3 + self.legsHeight4
