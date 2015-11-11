# Gregory Jerian
# Period 4
from math import sqrt
def main():
    try:
        print("This program finds every prime number less than or equal to n.")
        n = eval(input("Enter a value for n: "))
        while n > 2:
            x = 2
            numberPrime = "prime"
            while numberPrime == "prime" and x <= sqrt(n):
                if n % x == 0:
                    numberPrime = "not prime"
                else:
                    x = x + 1
            if numberPrime == "prime":
                print(n, end = " ")
            n = n - 1
        if n == 2:
            print("2", end = " ")
    except:
        print("Flippity-floopity error. Try un-flippity flooping the input.")

main()
