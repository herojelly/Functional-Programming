# Gregory Jerian
# Period 4
def main():
    print("This program finds the sum of a list of numbers.")
    numInput = input("Enter a list of numbers separated by commas: ")
    nums = numInput.split(",")
    print(sumList(nums))

def sumList(nums):
    x = 0
    for i in range(len(nums)):
        x = x + int(nums[i])
    return x

main()
