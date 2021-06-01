# Final Python Project
# Harpreet kaur, Harman
import sys

import Quadrilateral
from Parallelogram import Parallelogram
from Rectangle import Rectangle
from Square import Square
from Trapezoid import Trapezoid


def main():
    print("calling of main function")
    choice = ''
    while choice != '0':
        choice = input(""""
            S.Square
            R.Rectangle
            P.Parallelogram
            T.Trapezoid
            Q. Quadrilateral 
            E.Exit
            """"")
        if choice == 'S' or choice == 's':
            print("\n")
            # enter (7,4  7,26  29,26  29,4)
            xCoordinatePoint1 = int(input("Enter  x-coordinate first Point: "))
            yCoordinatePoint1 = int(input("Enter  y-coordinate first Point: "))

            xCoordinatePoint2 = int(input("Enter  x-coordinate second Point: "))
            yCoordinatePoint2 = int(input("Enter  y-coordinate second Point: "))

            xCoordinatePoint3 = int(input("Enter  x-coordinate third Point: "))
            yCoordinatePoint3 = int(input("Enter  y-coordinate third Point: "))

            xCoordinatePoint4 = int(input("Enter  x-coordinate fourth Point: "))
            yCoordinatePoint4 = int(input("Enter  y-coordinate fourth Point: "))

            # find area and  perimeter of a square
            print("\n")
            print("Area and  Perimeter of square")
            objSquare = Square(xCoordinatePoint1, xCoordinatePoint2, xCoordinatePoint3, xCoordinatePoint4,
                               yCoordinatePoint1, yCoordinatePoint2, yCoordinatePoint3, yCoordinatePoint4)

            print("distance" + str(objSquare.findDistance()))
            print("Area Of Square: " + str(objSquare.areaSquare()))
            print("Perimeter of Square: " + str(objSquare.perimeterSquare()))
            print("Draw of Square: " + str(objSquare.drawRectangle()))

        elif choice == 'R' or choice == 'r':
            print("\n")
            # enter (5,0 , -4,0, -4,-5, 5,-5)
            xCoordinatePoint1 = int(input("Enter  x-coordinate first Point: "))
            yCoordinatePoint1 = int(input("Enter  y-coordinate first Point: "))

            xCoordinatePoint2 = int(input("Enter  x-coordinate second Point: "))
            yCoordinatePoint2 = int(input("Enter  y-coordinate second Point: "))

            xCoordinatePoint3 = int(input("Enter  x-coordinate third Point: "))
            yCoordinatePoint3 = int(input("Enter  y-coordinate third Point: "))

            xCoordinatePoint4 = int(input("Enter  x-coordinate fourth Point: "))
            yCoordinatePoint4 = int(input("Enter  y-coordinate fourth Point: "))

            # Finding area and perimeter of Rectangle

            print("\n")
            print("Area and  Perimeter of Rectangle")
            objRectangle = Rectangle(xCoordinatePoint1, xCoordinatePoint2, xCoordinatePoint3, xCoordinatePoint4,
                                     yCoordinatePoint1, yCoordinatePoint2, yCoordinatePoint3, yCoordinatePoint4)

            print("DistanceBetweenXCoordinates: " + str(objRectangle.findDistanceBetweenXCoordinates()))
            print("DistanceBetweenYCoordinates: " + str(objRectangle.findDistanceBetweenYCoordinates()))
            print("Area Of Rectangle: " + str(objRectangle.areaRectangle()))
            print("Perimeter of Rectangle: " + str(objRectangle.perimeterRectangle()))
            print("Draw of Rectangle: " + str(objRectangle.drawRectangle()))

        elif choice == 'P' or choice == 'p':
            print("\n")
            # enter (−2,−1),(−1,2),(3,2),(2,−1) Or A(-4, -3) B(2, -3) C(4, -6) D(-2, -6)
            xCoordinatePoint1 = int(input("Enter  x-coordinate first Point: "))
            yCoordinatePoint1 = int(input("Enter  y-coordinate first Point: "))

            xCoordinatePoint2 = int(input("Enter  x-coordinate second Point: "))
            yCoordinatePoint2 = int(input("Enter  y-coordinate second Point: "))

            xCoordinatePoint3 = int(input("Enter  x-coordinate third Point: "))
            yCoordinatePoint3 = int(input("Enter  y-coordinate third Point: "))

            xCoordinatePoint4 = int(input("Enter  x-coordinate fourth Point: "))
            yCoordinatePoint4 = int(input("Enter  y-coordinate fourth Point: "))

            # Finding area and perimeter of Parallelogram

            print("\n")
            print("Area and  Perimeter of Parallelogram")
            objParallelogram = Parallelogram(xCoordinatePoint1, xCoordinatePoint2, xCoordinatePoint3,
                                             xCoordinatePoint4,
                                             yCoordinatePoint1, yCoordinatePoint2, yCoordinatePoint3,
                                             yCoordinatePoint4)
            print("base: "+str(objParallelogram.findBase()))
            print("height: "+str(objParallelogram.findHeight()))
            print("Draw Parallelogram: "+str(objParallelogram.drawParallelogram()))

            print("Area Of Parallelogram: " + str(objParallelogram.areaParallelogram()))
            print("Perimeter of Parallelogram: " + str(objParallelogram.perimeterParallelogram()))

        elif choice == 'T' or choice == 't':
            print("\n")
            # enter (6,7) (12,28) (34,28) (53,7)
            xCoordinatePoint1 = int(input("Enter  x-coordinate first Point: "))
            yCoordinatePoint1 = int(input("Enter  y-coordinate first Point: "))

            xCoordinatePoint2 = int(input("Enter  x-coordinate second Point: "))
            yCoordinatePoint2 = int(input("Enter  y-coordinate second Point: "))

            xCoordinatePoint3 = int(input("Enter  x-coordinate third Point: "))
            yCoordinatePoint3 = int(input("Enter  y-coordinate third Point: "))

            xCoordinatePoint4 = int(input("Enter  x-coordinate fourth Point: "))
            yCoordinatePoint4 = int(input("Enter  y-coordinate fourth Point: "))

            # Finding area and perimeter of Trapezoid
            print("\n")
            print("Area and  Perimeter of Trapezoid")
            objTrapezoid = Trapezoid(xCoordinatePoint1, xCoordinatePoint2, xCoordinatePoint3, xCoordinatePoint4,
                                     yCoordinatePoint1, yCoordinatePoint2, yCoordinatePoint3, yCoordinatePoint4)

            print("height: "+str(objTrapezoid.findHeightOfTrapezoid()))
            print("findBase41 (AD Base):  "+str(objTrapezoid.findBase41()))
            print("findBase43:  "+str(objTrapezoid.findBase43()))
            print("findBase32 (BC Base):  "+str(objTrapezoid.findBase32()))
            print("findBase21 : "+str(objTrapezoid.findBase21()))

            print("Area Of Trapezoid: " + str(objTrapezoid.areaTrapezoid()))
            print("Perimeter of Trapezoid: " + str(objTrapezoid.perimeterTrapezoid()))

            # print("Draw Parallelogram: "+str(objTrapezoid.drawTrapezoid()))

        elif choice == 'Q' or choice == 'q':
            print("\n")
            # enter (-1,3) (3,3) (5,-1) (-2,-1)
            xCoordinatePoint1 = int(input("Enter  x-coordinate first Point: "))
            yCoordinatePoint1 = int(input("Enter  y-coordinate first Point: "))

            xCoordinatePoint2 = int(input("Enter  x-coordinate second Point: "))
            yCoordinatePoint2 = int(input("Enter  y-coordinate second Point: "))

            xCoordinatePoint3 = int(input("Enter  x-coordinate third Point: "))
            yCoordinatePoint3 = int(input("Enter  y-coordinate third Point: "))

            xCoordinatePoint4 = int(input("Enter  x-coordinate fourth Point: "))
            yCoordinatePoint4 = int(input("Enter  y-coordinate fourth Point: "))

            # Finding area and perimeter of Quadrilateral
            print("\n")
            print("Area and  Perimeter of Quadrilateral")
            objQuadrilateral = Square(xCoordinatePoint1, xCoordinatePoint2, xCoordinatePoint3, xCoordinatePoint4,
                                      yCoordinatePoint1, yCoordinatePoint2, yCoordinatePoint3, yCoordinatePoint4)

            print("height 1: "+str(int(objQuadrilateral.findDistance1())))
            print("height 2 :  "+str(int(objQuadrilateral.findDistance2())))
            print("height 3:  "+str(int(objQuadrilateral.findDistance3())))
            print("height 4:  "+str(int(objQuadrilateral.findDistance4())))

            print("Area Of Quadrilateral: " + str(objQuadrilateral.areaQuadrilateral()))
            print("Perimeter of Quadrilateral: " + str(objQuadrilateral.perimeterQuadrilateral()))

        elif choice == 'E' or choice == 'e':
            sys.exit()
        else:
            print("Invalid choice ")


# Call the main function.
main()
