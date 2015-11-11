def main():
    z = 0
    print("This program adds a series of numbers entered by the user.")
    x = eval(input("How many numbers are to be added?: "))
    for i in range(x):
        y = eval(input("Enter one of the numbers: "))
        y = y + z
        z = y
    print("The sum of the numbers is", y)

main()
