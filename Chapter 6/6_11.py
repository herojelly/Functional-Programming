# Gregory Jerian
# Period 4
def main():
    print("This program squares a list of numbers.")
    numInput = input("Enter a list of numbers separated by commas: ")
    nums = numInput.split(",")
    print(squareEach(nums))
    

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = (int(nums[i]))**2
    return nums

main()
