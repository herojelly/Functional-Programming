import graphics
from graphics import *
import math
def main():
    # Introduction
    print("This program displays information about a triangle drawn by the user.")

    # Create a graphics window
    win = GraphWin("neato triangle")
    win.setCoords(0, 0, 10, 10)
    
    # Get inputs from the user and draw points
    broadcast = Text(Point(5, 0.5), "Click three points.")
    broadcast.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Create the triangle
    tri = Polygon(p1, p2, p3)
    tri.setFill("magenta")
    tri.setOutline("black")
    tri.draw(win)

    # Calculate distances of the sides
    d1x = p2.getX() - p1.getX()
    d2x = p3.getX() - p2.getX()
    d3x = p1.getX() - p3.getX()
    d1y = p2.getY() - p1.getY()
    d2y = p3.getY() - p2.getY()
    d3y = p1.getY() - p3.getY()
    d1l = math.sqrt((d1x ** 2) + (d1y ** 2))
    d2l = math.sqrt((d2x ** 2) + (d2y ** 2))
    d3l = math.sqrt((d3x ** 2) + (d3y ** 2))

    # Calculate perimeter, semiperimeter, and area
    P = d1l + d2l + d3l
    s = (d1l + d2l + d3l) / 2
    A = math.sqrt(s * (s - d1l) * (s - d2l) * (s - d3l))
    print("The perimeter of your triangle is", P, "and the area is", A)
    
    

main()
