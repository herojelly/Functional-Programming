# Gregory Jerian
# Period 4

def main():
    try:
        print("This program computes Easter for all years between 1900 and 2099.")
        year = eval(input("Enter a year: "))
        a = year%19
        b = year%4
        c = year%7
        d = (19*a + 24)%30
        e = (2*b + 4*c + 6*d + 5)%7
        if year < 1900 or year > 2099:
            print("Sorry, your year is not between 1900 and 2099.")
        elif year == 1954 or year == 1981 or year == 2049 or year == 2076:
            date = 15 + d + e
            if date <= 31:
                print("The date of Easter is March", date)
            else:
                print("The date of Easter is April", date - 31)
        else:
            date = 22 + d + e
            if date <= 31:
                print("The date of Easter is March", date)
            else:
                print("The date of Easter is April", date - 31)
    except:
        print("Sorry, that's not a valid input. Make sure it's a number.")
main()
