# Gregory Jerian
# Period 4

def main():
    print("This program calculates the total wages for a week.")
    
    try:
        hours = eval(input("Enter the number of hours worked: "))
        rate = eval(input("Enter the hourly rate for the job: "))
        if hours > 40:
            print("The total wage for the week is ${0:0.2f}".format((hours * rate) + (hours - 40) * rate * 0.5))
        else:
            print("The total wage for the week is ${0:0.2f}".format(hours * rate))
    except:
        print("There was an error. Make sure you enter numbers.")

main()
