# Gregory Jerian
# Period 4
def main():
    print("This program converts a list of strings to a list of ints.")
    Input = input("Enter a list of numbers separated by commas: ")
    strList = Input.split(",")
    print(toNumbers(strList))

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

main()
