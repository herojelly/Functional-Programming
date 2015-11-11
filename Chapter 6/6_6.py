# Gregory Jerian
# Period 4
import math
def main():
    print("This function computes the area of a triangle.")
    a, b, c = eval(input("Enter the lengths of its three sides: "))
    print("The area is", areaOfTriangle(a, b, c))
    myFile = open("triangle2.py", "w")
    print("The area is", areaOfTriangle(a,b, c), file = myFile)


def areaOfTriangle(a, b, c):
    s = (a + b + c)/2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return A

main()
