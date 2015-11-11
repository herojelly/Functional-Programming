def main():
    import math
    print("This program calculates the area of a triangle.")
    a, b, c = eval(input("Enter the lengths of its three sides separated by commas: "))
    s = (a + b + c)/2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("The area is", A)

main()
