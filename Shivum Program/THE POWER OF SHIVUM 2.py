from graphics import *
def main():
    shivum = "can't program"
    while shivum == "can't program":
        win = GraphWin("SHIVUM", 1000, 1000)
        win.setCoords(0,0,200,200)
        faceCircle = Circle(Point(100,100), 90)
        faceCircle.setFill("#351C1E")
        eye1 = Circle(Point(70, 70), 25)
        eye1.setFill("white")
        pupil1 = Circle(Point(70,70), 15)
        pupil1.setFill("black")
        eye2 = eye1.clone()
        eye2.move(55, 0)
        pupil2 = pupil1.clone()
        pupil2.move(55, 0)
        mouth = Rectangle(Point(60, 140), Point(140,150))
        mouth.setFill("black")
        faceCircle.draw(win)
        eye1.draw(win)
        eye2.draw(win)
        pupil1.draw(win)
        pupil2.draw(win)
        mouth.draw(win)
        print("LOL")
main()
