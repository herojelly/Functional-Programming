# Gregory Jerian
# Period 4
from math import sqrt
def main():
    try:
        print("This program determines if a number is prime.")
        number = eval(input("Enter a number to be tested: "))

        # Checks if the number is less than or equal to 2
        if number <= 2:
            if number == 2:
                print("The number is prime.")
            else:
                print("The number is not prime.")

        # If number > 2, then the code runs        
        else:
            x = 2
            numberPrime = "prime"
            while numberPrime == "prime" and x <= sqrt(number):
                if number % x == 0:
                    numberPrime = "not prime"
                else:
                    x = x + 1
            if numberPrime == "prime":
                print("The number is prime.")
            elif numberPrime == "not prime":
                print("The number is not prime.")
    except:
        print("Error! Make sure you enter a number.")

main()
