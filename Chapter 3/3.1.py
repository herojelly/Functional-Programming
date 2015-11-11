def main():
    import math
    print("This program calculates the volume and surface area of a sphere.")
    radius = eval(input("Enter the radius of the sphere: "))
    V = (4/3) * (math.pi) * (radius ** 3)
    A = 4 * (math.pi) * (radius ** 2)
    print("The volume is", V, "and the surface area is", A)

main()
