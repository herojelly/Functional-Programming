# Gregory Jerian
# Period 4

def main():
    print("This program determines eligibility for the Senate and House.")

    try:
        age = eval(input("Enter the person's age: "))
        yearsCitizen = eval(input("Enter the number of years this person has been a US citizen: "))
        if age >= 25 and yearsCitizen >= 7:
            print("This person is elligible for the House.")
        if age >= 30 and yearsCitizen >= 9:
            print("This person is elligible for the Senate.")
        elif age < 25 or yearsCitizen < 7:
            print("This person is not elligible for the Senate or the House.")
    except:
        print("Error! You typed something in wrong.")

main()
