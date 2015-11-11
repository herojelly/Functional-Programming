# Gregory Jerian
# Period 4
def main():
    # get the day month and year
    day, month, year = eval(input("Enter day, month, and year numbers: "))
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    print("The date is {0}/{1}/{2} or {3} {1}, {2}".format(month, day, year, months[month-1]))

main()
