# Final Python Project
# Harpreet kaur, Harman
import Quadrilateral
from Parallelogram import Parallelogram
from Rectangle import Rectangle
from Square import Square
from Trapezoid import Trapezoid


def main():
    print("calling of main function")

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

    print("Area Of Square: " + str(objSquare.areaSquare()))
    print("Perimeter of Square: " + str(objSquare.perimeterSquare()))

    # Finding area and perimeter of Rectangle
    print("\n")
    print("Area and  Perimeter of Rectangle")
    objRectangle = Rectangle(xCoordinatePoint1, xCoordinatePoint2, xCoordinatePoint3, xCoordinatePoint4,
                             yCoordinatePoint1, yCoordinatePoint2, yCoordinatePoint3, yCoordinatePoint4)

    print("Area Of Rectangle: " + str(objRectangle.areaRectangle()))
    print("Perimeter of Rectangle: " + str(objRectangle.perimeterRectangle()))

    # Finding area and perimeter of Parallelogram
    print("\n")
    print("Area and  Perimeter of Parallelogram")
    objParallelogram = Parallelogram(xCoordinatePoint1, xCoordinatePoint2, xCoordinatePoint3, xCoordinatePoint4,
                                     yCoordinatePoint1, yCoordinatePoint2, yCoordinatePoint3, yCoordinatePoint4)

    print("Area Of Parallelogram: " + str(objParallelogram.areaParallelogram()))
    print("Perimeter of Parallelogram: " + str(objParallelogram.perimeterParallelogram()))

    # Finding area and perimeter of Trapezoid
    print("\n")
    print("Area and  Perimeter of Trapezoid")
    objTrapezoid = Trapezoid(xCoordinatePoint1, xCoordinatePoint2, xCoordinatePoint3, xCoordinatePoint4,
                                 yCoordinatePoint1, yCoordinatePoint2, yCoordinatePoint3, yCoordinatePoint4)

    print("Area Of Parallelogram: " + str(objTrapezoid.areaTrapezoid()))
    print("Perimeter of Parallelogram: " + str(objTrapezoid.perimeterTrapezoid()))


# Call the main function.
main()
