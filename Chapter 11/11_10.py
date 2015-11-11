# Gregory Jerian
# Period 4

from math import sqrt

def main():
    try:
        # Intro and input
        print("This program finds all prime numbers up to some limit n.")
        n = eval(input("Enter some value for n: "))

        # Creates the list
        myList = []
        for i in range(n-1):
            myList.append(i+2)

        # Finds prime numbers
        while myList != []:
            number = myList[0]
            if number == 2:
                prime = True
                index = myList.index(number)
                print(myList.pop(index), end = " ")
                for number2 in myList:
                    if number2 % number == 0:
                        myList.remove(number2)
            else:
                x = 2
                prime = True
                while prime == True and x <= sqrt(number):
                    if number % x == 0:
                        prime = False
                    else:
                        x = x + 1
                if prime == True:
                    index = myList.index(number)
                    print(myList.pop(index), end = " ")
                    for number2 in myList:
                        if number2 % number == 0:
                            myList.remove(number2)
    except:
        print("Error! Make sure you enter a number.")
                        
main()
