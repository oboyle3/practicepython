a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# write a program that prints out all the elements
# of the list that are less than 5.
for x in a:
    if x < 5:
        print(f"..{x} <  5, so thats why we printed it..")


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Instead of printing the elements one by one,
# make a new list that has all the elements less than 5 from this list in it and print out this new list.
new_list = []
for x in a:
    if x < 5:
        print(f"..{x} <  5, so lets add it to new_list array..")
        new_list.append(x)

print(f"this is the new list {new_list}")

# Ask the user for a number and return a
# list that contains only elements from the original list a that are smaller than that number given by the user.
print(f"Enter a number and we will reveal what are lower than that number in the array")
some_num = int(input())
bogus_array = []
print(f"you selected {some_num}")
#check each element in the array is < some num and it to another array
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for z in a:
    if some_num > z:
        bogus_array.append(z)
print(f"{bogus_array} these are the ones that are in the array and lower")