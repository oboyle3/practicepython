# Write a program that asks the user how many Fibonnaci numbers 
# to generate and then generates them. Take this opportunity to
# think about how you can use functions. Make sure to ask the
# user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where 
#  the next number in the sequence is the sum of the previous two
#    numbers in the sequence.
#  The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
length = 5
first = 1
second = 1
new_num = 1
arr=[]
for x in range(length):
    # put ONE number into arr
    arr.append(first)
    new_num = first + second
    first = second
    second = new_num
    
    
# loop:
#     add the appropriate number to arr
#     calculate the new number
#     move first forward
#     move second forward
print(arr)
    


    

