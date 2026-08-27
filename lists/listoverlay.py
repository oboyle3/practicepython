# Take two lists, say for example these two:

b = [99, 1, 2, 89, 2, 2]
a = [99, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

store_common_list = []
#loop through a and say is the element in b?
#   yes? -> store in store_common_list = []
#   no? -> go to next element
for x in a:
    #check if x element we are checking  is in b
    #check if x was checked before -> ask is x already store common list array
    
        for b_element in b:
            if x not in store_common_list:
                if x == b_element:
                    print(f"we found a match! because x = {x} || b =  {b_element} and lets append array store_common_list = []")
                    store_common_list.append(x)
                    print(f"current commmon list = {store_common_list}")
        


print(f"this is the end list {store_common_list}")


#test case : what if we have duplicates in b?

