# Gregory Jerian
# Period 4

def main():
    print("This program calculates the grade of a quiz score.")
    
    try: 
        score = eval(input("Enter a quiz score between 0 and 5: "))
        if score == 0 or score == 1:
            print("You got an F.")
        elif score == 2:
            print("You got a D.")
        elif score == 3:
            print("You got a C.")
        elif score == 4:
            print("You got a B.")
        elif score == 5:
            print("You got an A.")
        else:
            print("That's not a valid number!")
    except:
        print("There was an error. Nuclear meltdown imminent.")

        
main()
