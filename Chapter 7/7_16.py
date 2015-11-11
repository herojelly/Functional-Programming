# Gregory Jerian
# Period 4

from graphics import *
from math import sqrt
def main():
    # Draw graphics window and target
    win = GraphWin("Archery")
    circle1 = Circle(Point(100,100),75)
    circle2 = Circle(Point(100,100),60)
    circle3 = Circle(Point(100,100),45)
    circle4 = Circle(Point(100,100),30)
    circle5 = Circle(Point(100,100),15)
    circle1.setFill("white")
    circle2.setFill("black")
    circle3.setFill("blue")
    circle4.setFill("red")
    circle5.setFill("yellow")
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    circle4.draw(win)
    circle5.draw(win)

    # processing loop
    total = 0
    for i in range(5):
        p = win.getMouse()
        p.setFill("orange")
        p.draw(win)
        x = p.getX()
        y = p.getY()
        if distance(x, y) <= 15:
            print("Bullseye! 9 points.")
            total = total + 9
        elif distance(x, y) > 15 and distance(x, y) <= 30:
            print("7 points.")
            total = total + 7
        elif distance(x, y) > 30 and distance(x, y) <= 45:
            print("5 points.")
            total = total + 5
        elif distance(x, y) > 45 and distance(x, y) <= 60:
            print("3 points.")
            total = total + 3
        elif distance(x, y) > 60 and distance(x, y) <= 70:
            print("1 point.")
            total = total + 1
        else:
            print("Miss! 0 points.")

    print("You got a total of", total, "points.")

def distance(x, y):
    distance = sqrt((x-100)**2 + (y-100)**2)
    return distance

main()
