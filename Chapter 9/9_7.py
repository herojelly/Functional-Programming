# Gregory Jerian
# Period 4

from random import randrange

def main():
    try:
        printIntro()
        n = getInputs()
        numWins = simNGames(n)
        printSummary(n, numWins)
    except:
        print("Error! Make sure that you are inputting a number.")

def printIntro():
    print("This program simulates multiple games of craps and")
    print("estimates the probability that the player wins.")

def getInputs():
    n = eval(input("How many games to simulate? "))
    return n

def simNGames(n):
    # Simulates n games of craps and returns the number of wins
    numWins = 0
    for i in range(n):
        diceTotal = randrange(1, 7) + randrange (1, 7)
        if diceTotal == 2 or diceTotal == 3 or diceTotal == 12:
            numWins = numWins
        elif diceTotal == 7 or diceTotal == 11:
            numWins = numWins + 1
        else:
            oldDiceTotal = diceTotal
            diceTotal = 0
            while diceTotal != oldDiceTotal and diceTotal != 7:
                diceTotal = randrange(1, 7) + randrange(1, 7)
                if diceTotal == oldDiceTotal:
                    numWins = numWins + 1
                elif diceTotal == 7:
                    numWins = numWins
    return numWins

def printSummary(n, numWins):
    print("\nGames simulated:", n)
    print("Wins: {0} ({1:0.1%})".format(numWins, numWins/n))

if __name__ == '__main__': main()
