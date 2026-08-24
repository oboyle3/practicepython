# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
print(f"enter num 1...")
num = int(input())
print(f"enter 'to divide by num' ...")
divide_num = int(input())

if num % divide_num == 0:
    print(f" {divide_num} divides into  {num}  ")
else:
    print(f"Come on man!")
    
