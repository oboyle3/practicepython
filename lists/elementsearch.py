
# Write a function that takes an ordered list of numbers (a list where the elements are 
# in order from smallest to largest) and another number. The function decides whether or
#  not the given number is inside the list and returns (then prints) an appropriate boolean
arr = [1,2,3,4,5]
num = 3
def funct(arr,num):
    if num in arr:
        print("true")
    else:
        print("false")

funct(arr,num)
