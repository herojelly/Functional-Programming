def main():
    print("This program calculates the slope of a line.")
    x1, y1 = eval(input("Enter the first coordinate in the form 'x, y': "))
    x2, y2 = eval(input("Enter the second coordinate in the form 'x, y': "))
    slope = (y2 - y1)/(x2 -x1)
    print("The slope is", slope)

main()
