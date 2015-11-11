# Gregory Jerian
# Period 4
def main():
    print("This program calculates the sum of the first n natural numbers and the sum")
    print("of the cubes of the first n natural numbers.")
    n = eval(input("Enter a value for n: "))
    print("The sum of the first n natural numbers is " + str(sumN(n)) + ".")
    print("The sum of the cubes of the first n natural numbers is " + str(sumNCubes(n)) + ".")

def sumN(n):
    x = 0
    for num in range(n):
        x = n + x
        n = n - 1
    return x

def sumNCubes(n):
    x = 0
    for num in range(n):
        x = n**3 + x
        n = n - 1
    return x

main()
