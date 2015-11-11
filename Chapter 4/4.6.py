import graphics
from graphics import *
def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Create a graphics window
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")

    # Get principal
    text1 = Text(Point(150, 80), "Enter the initial principal: ")
    text1.draw(win) 
    input = Entry(Point(150, 110), 10)
    input.setText("0.0")
    input.draw(win)
    button = Text(Point(150, 140), "Continue")
    button.draw(win)
    rect1 = Rectangle(Point(120, 130), Point(180, 150))
    rect1.draw(win)
    win.getMouse()
    principal = eval(input.getText())
    text1.undraw()
    button.undraw()
    input.undraw()
    rect1.undraw()

    # Get interest rate
    text2 = Text(Point(150, 80), "Enter the annualized interest rate: ")
    text2.draw(win)
    input = Entry(Point(150, 110), 10)
    input.setText("0.0")
    input.draw(win)
    button = Text(Point(150, 140), "Continue")
    button.draw(win)
    rect2 = Rectangle(Point(120, 130), Point(180, 150))
    rect2.draw(win)
    win.getMouse()
    apr = eval(input.getText())
    text2.undraw()
    button.undraw()
    input.undraw()
    rect2.undraw()

    # Draw labels on left edge
    Text(Point(20, 230), " 0.0K").draw(win)
    Text(Point(20, 180), " 2.5K").draw(win)
    Text(Point(20, 130), " 5.0K").draw(win)
    Text(Point(20, 80), " 7.5K").draw(win)
    Text(Point(20, 30), " 10.0K").draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11 + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    # Closing
    rect2 = Rectangle(Point(260, 220), Point(320, 240))
    rect2.setFill("cyan")
    rect2.draw(win)
    button = Text(Point(290, 230), "Done")
    button.draw(win)
    win.getMouse()
    win.close()

main()
