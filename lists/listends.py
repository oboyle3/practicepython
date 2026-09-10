# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list.
a = [5, 10, 15, 20, 25]
new = []
first = a[0]
len = 0
for x in a:
    len = len + 1
print(f"the len of the array called a  is {len}")
last = a[len -1]
new.append(first)
new.append(last)
print(f"the new array with first and last elements is {new}")