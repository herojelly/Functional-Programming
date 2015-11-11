def main():
    import math
    print("This program determines the length of a ladder when leaned against a house.")
    h = eval(input("Enter the height of the ladder: "))
    ad = eval(input("Enter the angle of the ladder in degrees: "))
    ar = math.pi/180 * ad
    l = h/math.sin(ad)
    print("The length of the ladder is", l)

main()
