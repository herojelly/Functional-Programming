# Gregory Jerian
# Period 4

def main():
    print("This program determines if the user is speeding.")

    try:
        speedLimit = eval(input("Enter the speed limit in mph: "))
        clockedSpeed = eval(input("Enter the clocked speed: "))
        if clockedSpeed > speedLimit:
            if clockedSpeed > 90:
                print("You were super speeding, so you will have to pay a fine of $" + str(250 + ((clockedSpeed - speedLimit) * 5)))
            else:
                print("You were speeding, so you will have to pay a fine of $" + str(50 + ((clockedSpeed - speedLimit) * 5)))
        else:
            print("You weren't speeding.")
    except:
        print("Error! You typed something in wrong.")

main()
