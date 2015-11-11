# Gregory Jerian
# Period 5

def main():
    try:
        print("This program computes fuel efficiency for a journey.")
        print("At any time, you may press <Enter> to quit.")
        startingDist = eval(input("Enter the starting odometer reading: "))
        avgMPG, x = 0, 1
        startingGas = 0
        userInput = input("Enter the odometer reading and amount of gas used separated by a space: ")
        while userInput != "":
            userInput = userInput.split()
            odometer, amtGas = eval(userInput[0]), eval(userInput[1])
            dist = odometer - startingDist
            amtGas = amtGas - startingGas
            MPG = dist/amtGas
            print("On Leg", x, "you achieved", MPG, "miles per gallon.")
            avgMPG = MPG + avgMPG
            x = x + 1
            startingDist = odometer
            amtGas = startingGas
            userInput = input("Enter the odometer reading and amount of gas used separated by a space: ")
        print("Your average MPG was", avgMPG/(x-1))
    except:
        print("Error! Make sure you are entering two numbers separated by a space.")
main()
