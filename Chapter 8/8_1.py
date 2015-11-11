# Gregory Jerian
# Period 4
def main():
    try:
        print("This program computes the nth Fibonacci number.")
        n = eval(input("Enter a value for n: "))
        print("The nth Fibonacci number is", str(fib(n)) + ".")
    except:
        print("Error! Looks like something went wrong.")

def fib(n):
    try:
        x = 1
        y = 1
        for num in range(n-2):
            z = x + y
            x = y
            y = z
        return y
    except:
        print("Error! Looks like something went wrong.")
main()
