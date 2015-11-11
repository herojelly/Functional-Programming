# Gregory Jerian
# Period 4
def main():
    print("This program counts the number of words in a sentence.")
    sentence = input("Enter a sentence: ")
    sentencelist = sentence.split(" ")
    sentencelength = len(sentencelist)
    print("There are", sentencelength, "words in this sentence.")

main()
