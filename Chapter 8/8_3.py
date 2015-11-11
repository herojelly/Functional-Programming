# Gregory Jerian
# Period 4

def main():
    try:
        shivum = "can program"
        while shivum == "can program":
            print("This program determines how long it will take for an investment to double.")
            r = eval(input("Enter the annualized interest rate: "))
            print("It will take", 2/r, "years for the investment to double.")
            shivum = "cool"
    except:
        print("Error. Make sure you input a number.")

main()
