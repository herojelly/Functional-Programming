# Gregory Jerian
# Period 4

def main():
    try:
        startingTime = input("Enter the starting time in form HH:MM:AM/PM ")
        endingTime = input("Enter the ending time in form HH:MM:AM/PM ")
        startingTime = startingTime.split(":")
        endingTime = endingTime.split(":")
        if startingTime[2] == "AM":
            startingTime = int(startingTime[0])*60 + int(startingTime[1])
        elif startingTime[2] == "PM":
            startingTime = int(startingTime[0])*60 + int(startingTime[1]) + 12*60
        else:
            print("Error. Try inputting either AM or PM.")
        if endingTime[2] == "AM":
            endingTime = int(endingTime[0])*60 + int(endingTime[1])
        elif endingTime[2] == "PM":
            endingTime = int(endingTime[0])*60 + int(endingTime[1]) + 12*60
        else:
            print("Error. Try inputting either AM or PM.")

        ninePM = 1260
        if endingTime < startingTime:
            print("Error. Your ending time is greater than your starting time.")
        elif startingTime >= ninePM and endingTime >= ninePM:
            total = (endingTime - startingTime)/60 * 1.75
            print("The total babysitting bill is ${0:0.2f}".format(total))
        elif startingTime < ninePM and endingTime < ninePM:
            total = (endingTime - startingTime)/60 * 2.5
            print("The total babysitting bill is ${0:0.2f}".format(total))
        elif startingTime < ninePM and endingTime >= ninePM:
            total = ((ninePM - startingTime)/60 * 2.5) + ((endingTime - ninePM)/60 * 1.75)
            print("The total babysitting bill is ${0:0.2f}".format(total))
    except:
        print("There was an error. Make sure to input in form HH:MM:AM/PM.")
main()
