# Gregory Jerian
# Period 4

from random import randrange

def main():
    print("This program shuffles a list in a random order.")
    myList = input("Enter a list separated by spaces: ")
    myList = myList.split()
    print(shuffle(myList))

def shuffle(myList):
    newList = []
    n = 0
    for i in range(len(myList)):
        value = randrange(0, len(myList))
        newList.append(myList[value])
        del myList[value]
        n = n - 1
    return newList

main()
    
