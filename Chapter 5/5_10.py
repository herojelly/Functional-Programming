# Gregory Jerian
# Period 4
def main():

    # initialize variables
    print("This program calculates the average word length in a sentence.")
    sentence = input("Enter a sentence: ")
    sentenceList = sentence.split(" ")
    sentenceLength = len(sentenceList)

    # loop
    x = 0
    avgNumerator = 0
    for num in range(sentenceLength):
        wordLength = len(sentenceList[x])
        x = x + 1
        avgNumerator = avgNumerator + wordLength

    # display outputs
    avg = avgNumerator/sentenceLength
    print("The average word length in this sentence is", str(avg) + ".")

main()
