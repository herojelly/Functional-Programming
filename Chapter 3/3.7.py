def main():
    import math
    print("This program determines the distance between two points.")
    x1, y1 = eval(input("Enter the first coordinate in the form 'x, y': "))
    x2, y2 = eval(input("Enter the second coordinate in the form 'x, y': "))
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    print("The distance is", distance)

main()
