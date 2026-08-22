# odd or even Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user
import time
print(f"enter a number, we will tell you if even or odd...")
entered_num = int(input())

#tell user if even or odd 
# if 3 % 4 == 0
if entered_num % 2   == 0:
    time.sleep(.3)
    print(f"the number you entered is even")
    print(f"lets check of this num is a multiple of 4...")
    if entered_num % 4 == 0:
        print(f" multiple of 4 and even ")
elif entered_num % 2 != 0:
    print(f"you entered a odd num....")
# elif entered_num % 4 == 0:
#         print(f"this number yournentered is a multiple of 4")


# If the number is a multiple of 4, print out a different message.