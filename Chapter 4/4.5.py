import graphics
from graphics import *
def main():
    #creating the window
    win = graphics.GraphWin("Oh baby a straight")
    win.setCoords(0, 0, 400, 400)

    #creating/cloning dice
    die1 = Rectangle(Point(30,200), Point(80,250)).draw(win)
    die2 = Rectangle(Point(105,200), Point(155,250)).draw(win)
    die3 = Rectangle(Point(180,200), Point(230,250)).draw(win)                    
    die4 = Rectangle(Point(255,200), Point(305,250)).draw(win)
    die5 = Rectangle(Point(330,200), Point(380,250)).draw(win)

    #adding dots
    pt1 = Point(55, 225).draw(win)
    pt21 = Point(121.67, 216.67).draw(win)
    pt22 = Point(138.33, 233.33).draw(win)
    pt31 = Point(205, 225).draw(win)
    pt32 = Point(196.67, 216.67).draw(win)
    pt33 = Point(213.33, 233.33).draw(win)
    pt41 = Point(271.67, 216.67).draw(win)
    pt42 = Point(288.33, 216.67).draw(win)
    pt43 = Point(271.67, 233.33).draw(win)
    pt44 = Point(288.33, 233.33).draw(win)
    pt51 = Point(346.67, 216.67).draw(win)
    pt52 = Point(346.67, 233.33).draw(win)
    pt53 = Point(363.33, 216.67).draw(win)
    pt54 = Point(363.33, 233.33).draw(win)
    pt55 = Point(355, 225).draw(win)
    

main()
