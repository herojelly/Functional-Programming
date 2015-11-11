def main():
    fact = 0
    print("This program finds the sum of the cubes of the first n natural numbers.")
    n = eval(input("Enter a value for n: "))
    for number in range(n+1):
        fact = fact + number ** 3
    print(fact)

main()
