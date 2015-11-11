# Gregory Jerian
# Period 4
from graphics import *
def main():
    print("This program draws a face given a center, size, and window.")
    x, y = eval(input("Enter the center of the face in form x, y: "))
    size = eval(input("Enter the size/radius of the face: "))
    win = input("Enter the name of the graphics window: ")
    drawFace(x, y, size, win)

def drawFace(x, y, size, win):
    win = GraphWin(win)
    faceCircle = Circle(Point(x, y), size)
    faceCircle.setFill("#351C1E")
    eye1 = Circle(Point((0.7 * x), (0.7 * y)), (0.28 * size))
    eye1.setFill("white")
    pupil1 = Circle(Point((0.7 * x), (0.7 * y)), (0.17 * size))
    pupil1.setFill("black")
    eye2 = eye1.clone()
    eye2.move((0.55 * x), 0)
    pupil2 = pupil1.clone()
    pupil2.move((.55 * x), 0)
    mouth = Rectangle(Point((0.6 * x), (1.4 * y)), Point((1.4*x),(1.5*y)))
    mouth.setFill("black")

    faceCircle.draw(win)
    eye1.draw(win)
    eye2.draw(win)
    pupil1.draw(win)
    pupil2.draw(win)
    mouth.draw(win)

main()
