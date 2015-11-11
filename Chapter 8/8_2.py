# Gregory Jerian
# Period 4

def main():
    print("This program computes the windchill index.")

    # V is wind speed in mph and T is temperature in degrees Fahrenheit.
    
    # prints the row of wind speed
    V = 0
    print(end = "        ")
    for Shivums in range(11):
        print("{0:<8}".format(V), end = "")
        V = V + 5

    # prints the column of temperatures and all the results
    T = -20
    V = 0
    print("")
    for Sids in range(9):
        VList = []
        for Jerrys in range(11):
            VList.append(index(V, T))
            V = V + 5
        print("{0:>3} {1:>7} {2:>7.2f} {3:>7.2f} {4:>7.2f} {5:>7.2f} {6:>7.2f} {7:>7.2f} {8:>7.2f} {9:>7.2f} {10:>7.2f} {11:>7.2f}".format(T, "N/A", VList[1], VList[2], VList[3], VList[4], VList[5], VList[6], VList[7], VList[8], VList[9], VList[10]))
        T = T + 10 

# calculates windchill index
def index(V, T):
    windChill = 35.74 + (0.6215*T) - (35.75*V**0.16) + (0.4725*T*V**0.16)
    return windChill

main()
