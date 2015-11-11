import graphics
from graphics import *
def main():
    win = GraphWin("neato target")
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

main()
