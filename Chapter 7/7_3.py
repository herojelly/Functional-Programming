# Gregory Jerian
# Period 4

def main():
    print("This program calculates a grade given an exam score.")

    try:
        score = eval(input("Enter an exam score between 0 and 100: "))
        if score < 60:
            print("You got an F.")
        elif score >= 60 and score < 70:
            print("You got a D.")
        elif score >= 70 and score < 80:
            print("You got a C.")
        elif score >= 80 and score < 90:
            print("You got a B.")
        elif score >= 90 and score <= 100:
            print("You got an A.")
        else:
            print("Error! That's not a valid exam score.")
    except:
        print("Error! Looks like you messed that input up. Try again.")

main()
