# Gregory Jerian
# Period 4
from graphics import *
def main():
    win = GraphWin("Circle Mover")
    shape = Circle(Point(100,100), 50)
    shape.setFill("peachpuff")
    shape.setOutline("black")
    shape.draw(win)
    Text(Point(100,180), "Click anywhere to move the circle.").draw(win)
    for i in range(10):
        point = win.getMouse()
        newCenter = Point(point.getX(), point.getY())
        shape = moveTo(shape, newCenter)
        shape.draw(win)
    

def moveTo(shape, newCenter):
    shape.undraw()
    shape = Circle(newCenter, 50)
    shape.setFill("peachpuff")
    shape.setOutline("black")
    return shape

main()
