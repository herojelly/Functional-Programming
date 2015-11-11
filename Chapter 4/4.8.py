import graphics
from graphics import *
import math
def main():

    # Introduction
    print("This program allows the user to draw a line segment and then displays")
    print("some graphical and textual information about the line segment.")

    # Graphing Window
    win = GraphWin("Line Segment Info")
    win.setCoords(-10, -10, 10, 10)

    # Input
    message = Text(Point(0, 8), "Click in two places with your mouse.")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    # Create Line Segment and Midpoint
    line = Line(p1, p2)
    line.draw(win)
    midptX = ((p1.getX() + p2.getX()) / 2)
    midptY = ((p1.getY() + p2.getY()) / 2)
    midpt = Point(midptX, midptY)
    midpt.setFill("cyan")
    midpt.draw(win)

    # Calculate Length and Slope
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    slope = dy/dx
    length = math.sqrt((dx ** 2) + (dy ** 2))

    print("The midpoint of the line has been marked.")
    print("The length of the line is", length, "and the slope is", slope)

main()
