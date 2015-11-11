# Gregory Jerian
# Period 4
def main():
    print("This program computes the nth Fibonacci number.")
    n = eval(input("Enter a value for n: "))
    print("The nth Fibonacci number is", str(fib(n)) + ".")

def fib(n):
    x = 1
    y = 1
    for num in range(n-2):
        z = x + y
        x = y
        y = z
    return y
main()
