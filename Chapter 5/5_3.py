# Gregory Jerian
# Period 4
def main():
    score = eval(input("Enter an exam score: "))
    grades = ["F", "F", "F", "F", "F", "F", "F", "F", "F",
              "F", "F", "F", "F", "F", "F", "F", "F", "F",
              "F", "F", "F", "F", "F", "F", "F", "F", "F",
              "F", "F", "F", "F", "F", "F", "F", "F", "F",
              "F", "F", "F", "F", "F", "F", "F", "F", "F",
              "F", "F", "F", "F", "F", "F", "F", "F", "F",
              "F", "F", "F", "F", "F", "F", "D", "D", "D",
              "D", "D", "D", "D", "D", "D", "D", "C", "C",
              "C", "C", "C", "C", "C", "C", "C", "C", "B",
              "B", "B", "B", "B", "B", "B", "B", "B", "B",
              "A", "A", "A", "A", "A", "A", "A", "A", "A",
              "A", "A",]
    print("Congratulations, you got a " + grades[score])
    
main()
