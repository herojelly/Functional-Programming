# Gregory Jerian
# Period 4

from graphics import *
import math
def main():
    
    try:
        # Introduction
        print("This program computes the intersection of a circle with a horizontal")
        print("line and displays the information textually and graphically.")

        # Input
        r = eval(input("Enter the radius of the circle: "))
        b = eval(input("Enter the y-intercept of the line: "))

        # Window
        win = GraphWin("Circle Intersection")
        win.setCoords(-10, -10, 10, 10)

        # Circle
        cir = Circle(Point(0, 0), r)
        cir.draw(win)

        # Line
        line = Line(Point(-10, b), Point(10, b))
        line.draw(win)

        # Intersection
        try:
            x = math.sqrt((r ** 2) - (b ** 2))
            b = float(b)
            print("The intersections are (", -x, ",", b, ") and (", x,",", b, ")")
        except:
            print("The line does not interesect the circle.")
    except:
        print("Error! You inputted something wrong.")
main()
