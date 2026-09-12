# Write a program  takes a list
# and returns a new list that contains all the elements of the first list minus all the duplicates
given_list = ["Pat", "Henry", "Pat", "Thomas"]
new = []
for x in given_list:
    #check if x is in the list and if not add it to the new array
    if x in new:
        print(f"{x} already in given list")
    else:
        print(f"lets add {x} to the new array")
        new.append(x)
print(f"new array = {new}")