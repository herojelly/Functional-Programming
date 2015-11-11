# Gregory Jerian
# Period 4
def main():
    print("This program calculates the future value of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years of the investment: "))

    print(" ")
    print("{0:<} {1:^10}".format("Year", "Value"))
    print("---------------")
    yearNum = 0
    for i in range(years + 1):
        print("{0:^5} ${1:<10.2f}".format(yearNum, principal))
        principal = principal * (1 + apr)
        yearNum = yearNum + 1

main()
