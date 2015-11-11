# Gregory Jerian
# Period 4
def main():
    phrase = input("Enter a phrase: ")
    phraselist = phrase.split(" ")
    phraselength = len(phraselist)
    n = 0
    for num in range (phraselength):
        entry = (phraselist[n])
        entry = entry[0].upper()
        print(entry, end="")
        n = n + 1

main()
