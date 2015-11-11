# Gregory Jerian
# Period 4

def main():
    print("This program determines if a year is a leap year.")

    try:
        year = eval(input("Enter the year: "))
        if year % 4 != 0:
            print("That's not a leap year.")
        elif year % 100 == 0:
            if year % 400 == 0:
                print("Yes, that's a leap year.")
            else:
                print("That's not a leap year.")
        elif year % 4 == 0:
            print("Yes, that's a leap year.")
    except:
        print("Error! Try inputting something else.")

main()
