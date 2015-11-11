# Gregory Jerian
# Period 4

from random import randrange

def main():
    try:
        printIntro()
        n = getInputs()
        numFOAK = simNRolls(n)
        printSummary(n, numFOAK)
    except:
        print("Error! Make sure that you are inputting a number.")

def printIntro():
    print("This program performs a simulation to estimate the probability")
    print("of rolling five-of-a-kind in a single roll of five dice.")

def getInputs():
    n = eval(input("How many rolls to simulate? "))
    return n

def simNRolls(n):
    # Simulates n rolls of dice and returns the number of five-of-a-kinds
    numFOAK = 0
    for i in range(n):
        roll1 = simOneRoll()
        roll2 = simOneRoll()
        roll3 = simOneRoll()
        roll4 = simOneRoll()
        roll5 = simOneRoll()
        if roll1 == roll2 == roll3 == roll4 == roll5:
            numFOAK = numFOAK + 1
    return numFOAK

def simOneRoll():
    return randrange(1, 7)

def printSummary(n, numFOAK):
    print("\nRolls simulated:", n)
    print("Five-of-a-kinds: {0} ({1:0.3%})".format(numFOAK, numFOAK/n))

if __name__ == '__main__': main()
