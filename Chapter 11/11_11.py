# Gregory Jerian
# Period 4

def main():
    try:
        print("This program censors all the four-letter words in a file.")

        # get the file names
        infileName = input("Enter the name of the file: ")
        outfileName = input("What file should the censored text go in? ")
        
        # open the files
        infile = open(infileName, "r")
        outfile = open(outfileName, "w")

        # process each line of the input file
        for line in infile:
            myList = line.split()
            for i in range(len(myList)):
                if len(myList[i]) == 4:
                    print("****", end = " ", file=outfile)
                else:
                    print(myList[i], end = " ", file=outfile)
    except:
        print("Error. Make sure you type in the file names right!")
    
main()
