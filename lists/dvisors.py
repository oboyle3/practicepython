# Create a program that asks the user for a number and then prints out 
# a list of all the divisors of that number. (If you don’t know what a
#  divisor is, it is a number that divides evenly into another number
#      For example, 13 is a divisor of 26 because 26 / 13 has no remainder.) 
num = 26
num_input = 13
test = (26 % 13)
fake_array = []
for x in range(1, num):
    if 26 % x == 0:
        print(f" {x} is a divior of {num} lets store it")
        fake_array.append(x)
print(f"array with all the diviors = {fake_array}")
print(26 % 13)