# Gregory Jerian
# Period 4
def main():
    print("This program illustrates a chaotic function.")
    x, y = eval(input("Enter two numbers between 0 and 1: "))
    numIterations = eval(input("Enter the number of iterations: "))

    # chart creation
    print(" ")
    print("{0:^} {1:^7} {2:^10}".format("index", x, y))
    print("---------------------------")
    indexNum = 1
    for i in range(numIterations):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{0:^3} {1:^10.6f} {2:^5.6f}".format(indexNum, x, y))
        indexNum = indexNum + 1

main()
