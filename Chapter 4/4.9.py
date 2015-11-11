import graphics
from graphics import *
def main():
    # Introduction
    print("This program displays information about a rectangle drawn by the user.")

    # Create a graphics window
    win = GraphWin("neato rectangle")
    win.setCoords(0, 0, 10, 10)
    
    # Get inputs from the user and draw points
    broadcast = Text(Point(5, 0.5), "Click two points.")
    broadcast.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    # Create the rectangle
    rect = Rectangle(p1, p2)
    rect.setFill("magenta")
    rect.setOutline("black")
    rect.draw(win)

    # Calculate perimeter and area
    l = abs(p2.getX() - p1.getX())
    h = abs(p2.getY() - p1.getY())
    P = (2 * l) + (2 * h)
    A = l * h
    print("The perimeter of your rectangle is", P, "and the area is", A)
    
    

main()
