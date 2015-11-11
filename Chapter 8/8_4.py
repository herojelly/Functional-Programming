# Gregory Jerian
# Period 4

def main():
    try:
        print("This program applies the Syracuse sequence to a number.")
        x = int(input("Enter a natural number: "))
        if x <= 0:
            print("That's not a natural number.")
        else:
            print(x, end = " ")
            while x > 1:
                if x % 2 == 0:
                    x = int(x/2)
                    print(x, end = " ")
                else:
                    x = 3*x + 1
                    print(x, end = " ")
    except:
        print("That's not a natural number.")

main()
