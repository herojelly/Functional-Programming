# Gregory Jerian
# Period 4
def main():
    print("This program finds the acronym of a phrase.")
    phrase = input("Enter a phrase: ")
    print(acronym(phrase))

def acronym(phrase):
    phraselist = phrase.split(" ")
    phraselength = len(phraselist)
    n = 0
    acronym = ""
    for num in range (phraselength):
        entry = (phraselist[n])
        entry = entry[0].upper()
        n = n + 1
        acronym = acronym + str(entry)
    return acronym

main()
