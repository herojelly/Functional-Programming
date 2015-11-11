# Gregory Jerian
# Period 4

def main():
    try:
        print("This program computes Easter for all years between 1982 and 2048.")
        year = eval(input("Enter a year: "))
        if year < 1982 or year > 2048:
            print("Sorry, your year is not between 1982 and 2048.")
        else:
            a = year%19
            b = year%4
            c = year%7
            d = (19*a + 24)%30
            e = (2*b + 4*c + 6*d + 5)%7
            date = 22 + d + e
            if date <= 31:
                print("The date of Easter is March", date)
            else:
                print("The date of Easter is April", date - 31)
    except:
        print("Sorry, that's not a valid input. Make sure it's a number.")
main()
