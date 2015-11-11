# Gregory Jerian
# Period 4

def main():
    print("This program removes duplicate values from a list.")
    somelist = input("Enter a list of values separated by spaces: ")
    somelist = somelist.split()
    print(removeDuplicates(somelist))

def removeDuplicates(somelist):
    otherList = []
    for i in somelist:
        if i not in otherList:
            otherList.append(i)
    return otherList

main()
