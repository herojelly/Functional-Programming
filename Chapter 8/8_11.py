# Gregory Jerian
# Period 5

def main():
    try:
        print("This program determines the running total of cooling and heating degree-days.")
        temp = input("Enter the first temperature: (<Enter> to quit) ")
        coolDays, heatDays = 0, 0
        while temp != "":
            if eval(temp) < 60:
                heatDays = (60 - eval(temp)) + heatDays
                temp = input("Enter another temperature: (<Enter> to quit) ")
            elif eval(temp) > 80:
                coolDays = (eval(temp) - 80) + coolDays
                temp = input("Enter another temperature: (<Enter> to quit) ")
            else:
                temp = input("Enter another temperature: (<Enter> to quit) ")       

        print("The temps of the cooling degree-days were", coolDays)
        print("The temps of the heating degree-days were", heatDays)
    except:
        print("Looks like there was an error. Make sure you're inputting numbers.")
    
main()
