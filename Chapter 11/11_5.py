# Gregory Jerian
# Period 4

def main():
    print("This program showcases several functions that modify lists.")
    userInput = input("Enter a list separated by spaces: ")
    myList = userInput.split()
    print("\nChoose a function by typing in the corresponding number.")
    print("(1) Count")
    print("(2) Is in")
    print("(3) Index")
    print("(4) Reverse")
    print("(5) Sort (Strings only)")
    userChoice = int(input("\nEnter a number: "))
    if userChoice == 1:
        print("\nCount function activated.")
        x = input("What would you like to count the number of in this list? ")
        count(myList, x)
    elif userChoice == 2:
        print("\nIs in function activated.")
        x = input("What would you like to look for in this list? ")
        isin(myList, x)
    elif userChoice == 3:
        print("\nIndex function activated.")
        x = input("What would you like to search for the index of in this list? ")
        index(myList, x)
    elif userChoice == 4:
        print("\nReverse function activated.")
        reverse(myList)
    elif userChoice == 5:
        print("\nSort function activated.")
        sort(myList)
    else:
        print("Error! Type a number between 1 and 5.")

def count(myList, x):
    numOfX = 0
    swag = 0
    for entry in myList:
        if str(myList[swag]) == x:
            numOfX = numOfX + 1
        swag = swag + 1
    print("There are", numOfX, "copies of that in this list.")

def isin(myList, x):
    isXThere = False
    swag = 0
    for entry in myList:
        if str(myList[swag]) == x:
            isXThere = True
        swag = swag + 1
    if isXThere:
        print("Yes,", x, "is in that list.")
    else:
        print("No,", x, "is not in that list.")

def index(myList, x):
    isXThere = False
    swag = 0
    try:
        while not isXThere:
            if str(myList[swag]) == x:
                isXThere = True
                print("The first occurence of that is found at index", swag)
            swag = swag + 1
    except:
        print("That does not occur in the list.")

def reverse(myList):
    newList = []
    length = len(myList) - 1
    for i in range(len(myList)):
        newList.append(myList[length])
        length = length - 1
    print(newList)

def sort(myList):
    listLength = len(myList)
    newList = []
    for n in range(listLength):
        ordList = []
        word = myList[n]
        wordLength = len(myList[n])
        for i in range(wordLength):
            letter = word[i]
            ordList.append(ord(letter))
        total = 0
        for g in range(len(ordList)):
            total = ordList[g] + total
        newList.append(total)

    newestList = []
    for y in range(len(newList)):
        newestList.append(min(myList))
        myList.remove(min(myList))

    print(newestList)
            
main()
