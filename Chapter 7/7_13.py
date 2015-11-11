# Gregory Jerian
# Period 4

def main():
    print("This program determines the number of a day of the year.")
    invalidMonth = 0
    invalidYear = 0
    invalidDay = 0

    try:
        # Gets month, day, year
        date = input("Enter a date in form MM/DD/YYYY: ")
        date = date.split("/")
        month, day, year = int(date[0]), int(date[1]), int(date[2])

        # Calculates if it is a leap year
        # if leapyear = 0 it is a leap year, if leapyear = 1 it is not a leap year
        if year % 4 != 0:
            leapyear = 1
        elif year % 100 == 0:
            if year % 400 == 0:
                leapyear = 0
            else:
                leapyear = 1
        elif year % 4 == 0:
            leapyear = 0

        # Calculates validity of month
        if month < 1 or month > 12:
            print("Invalid month.")
            invalidMonth = 1
            
        # Calculates validity of day
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day > 31 or day < 1:
                print("Invalid day.")
                invalidDay = 1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30 or day < 1:
                print("Invalid day.")
                invalidDay = 1
        elif month == 2 and leapyear == 0:
            if day > 29 or day < 1:
                print("Invalid day.")
                invalidDay = 1
        elif month == 2 and leapyear == 1:
            if day > 28 or day < 1:
                print("Invalid day.")
                invalidDay = 1
        else:
            print("Invalid day.")
            invalidDay = 1
                    
        # Calculates the validity of the year
        if year < 1:
            print("Invalid year.")
            invalidYear = 1

        # If the date is valid the program continues
        if invalidMonth == 0 and invalidDay == 0 and invalidYear == 0:
            dayNum = 31 * (month - 1) + day
            if month > 2:
                dayNum = dayNum - (4*month + 23)//10
                if leapyear == 0:
                    dayNum = dayNum + 1
                    print("The day number is", dayNum)
                else:
                    print("The day number is", dayNum)
            else:
                print("The day number is", dayNum)

    except:
        print("Invalid date. Make sure you use the format MM/DD/YYYY.")

main()
