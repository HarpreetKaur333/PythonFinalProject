# Final Python Project
# Harpreet kaur, Harman
import Quadrilateral
from Square import Square


def main():
    print("calling of main function")
    # find area and  perimeter of a square
    objBaseCls = Quadrilateral

    sLength = int(input("Enter Length of any one side: "))
    objSquare = Square(sLength, "", "", "", "", "", "", "", "", "", "")
    print("The Area of Square is: " + objSquare.areaSquare())
    print("The perimeter of a Square is: " + objSquare.perimeterSquare())
    print("\n")


# Call the main function.
main()
