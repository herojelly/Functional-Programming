def main():
    import math
    print("This program finds the Gregorian epact.")
    year = eval(input("Enter the year: "))
    C = year//100
    epact = (8 + (C//4) - C + ((8 * C + 13)//25) + 11 * (year%19))%30
    print("The epact is", epact)

main()
