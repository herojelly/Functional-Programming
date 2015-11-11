def main():
    print("This program determines the distance to a lightning strike.")
    s = eval(input("Enter the time elapsed between the flash and the sound of thunder: "))
    mi = s * 1100 / 5280
    print("The distance to the lightning strike is", mi, "miles.")
    
main()
