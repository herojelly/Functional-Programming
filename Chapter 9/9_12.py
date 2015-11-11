# Gregory Jerian
# Period 4

from random import randrange

def main():
    try:
        printIntro()
        n = getInputs()
        numSteps = simNSteps(n)
        printSummary(n, numSteps)
    except:
        print("Error! Make sure that you are inputting a number.")

def printIntro():
    print("This program simulates a random walk of n steps.")

def getInputs():
    n = eval(input("How many steps to simulate? "))
    return n

def simNSteps(n):
    # Simulates n steps and returns the distance from the original location
    numSteps = 0
    for i in range(n):
        direction = simOneStep()
        if direction == "forward":
            numSteps = numSteps + 1
        elif direction == "backwards":
            numSteps = numSteps - 1
    return abs(numSteps)

def simOneStep():
    randNum = randrange(0, 2)
    if randNum == 0:
        return "forward"
    elif randNum == 1:
        return "backwards"

def printSummary(n, numSteps):
    print("\nSteps simulated:", n)
    print("Steps away from starting location:", numSteps)

main()
