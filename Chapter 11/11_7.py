# Gregory Jerian
# Period 4

def main():
    try:
        # Intro
        print("This function computes the inner product of 2 lists.")
        print("At any time, you may press <Enter> to end.")

        # Get the inputs using a sentinel loop
        x, y = 0, 0
        xList, yList = [], []
        pair = input("Enter the first ordered pair in form x,y: ")
        pair = pair.split(",")
        x, y = pair[0], pair[1]
        while x != "":
            y = pair[1]
            xList.append(eval(x))
            yList.append(eval(y))
            pair = input("Enter an ordered pair in form x,y: ")
            pair = pair.split(",")
            x = pair[0]
            
        print(innerProd(xList, yList))
    except:
        print("Error. Make sure you are entering numbers.")

def innerProd(xList, yList):
    try:
        # Multiply together the x and y values of each ordered pair
        newList = []
        for i in range(len(xList)):
            newList.append(xList[i] * yList[i])

        # Add everything up
        total = 0
        for n in range(len(newList)):
            total = total + newList[n]

        return total
    except:
        print("Error. Make sure you are entering numbers.")

main()
