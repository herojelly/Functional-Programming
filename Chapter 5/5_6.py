# Gregory Jerian
# Period 4
def main():
    # intro
    print("This program determines the value of a name.")
    
    # initialize variables
    name = input("Enter your name: ")
    namelength = len(name)
    name = name.lower()
    namelist = name.split(" ")
    listlength = len(namelist)

    # processing loop
    n = 0
    x = 0
    for gregorys in range(listlength):
        word = namelist[n]
        wordlength = len(namelist[n])
        n = n + 1
        y = 0
        for gregorys in range(wordlength):
            letter = word[y]
            x = (x + ord(letter)) - 96
            y = y + 1

    print("The numeric value is " + str(x) + ".")

main()
