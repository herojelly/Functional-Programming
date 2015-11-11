# Gregory Jerian
# Period 4

from random import randrange

def main():
    try:
        printIntro()
        n = getInputs()
        wins, losses = simNGames(n)
        printSummary(n, wins, losses)
    except:
        print("Error! Make sure that you are inputting a number.")

def printIntro():
    print("This program simulates a game of blackjack from the point of view")
    print("of the dealer and predicts the probability the dealer will bust.")

def getInputs():
    n = eval(input("How many games of blackjack to simulate? "))
    return n

def simNGames(n):
    # Simulates n games of blackjack
    wins = 0
    losses = 0
    for i in range(n):
        score = simOneGame()
        if score <= 21:
            wins = wins + 1
        else:
            losses = losses + 1
    return wins, losses

def simOneGame():
    score = 0
    while not gameOver(score):
        card, hasAce = drawACard()
        if card == "ace" and hasAce == True:
            if score >= 6 and score <= 10:
                score = score + 11
            else:
                score = score + 1
        else:
            score = score + card
    return score
    
def drawACard():
    card = randrange(1, 14)
    if card == 1:
        return "ace" , True
    elif card == 11 or card == 12 or card == 13:
        return 10, False
    else:
        return card, False

def gameOver(score):
    return (score >= 17 and score <= 21) or score >= 22

def printSummary(n, wins, losses):
    print("\nGames simulated:", n)
    print("Wins: {0} ({1:0.1%})".format(wins, wins/n))
    print("Busts: {0} ({1:0.1%})".format(losses, losses/n))
    
if __name__ == '__main__': main()
