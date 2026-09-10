# user_input = int(input("enter a num"))
# print(user_input)
num = 13
test_num =6
#prime is only 1 and itself are prime
def is_prime(num):
    for x in range(2,num):
        curr = num % x
        if num % x == 0:
            print(f"not prime because {num} % {x} = {curr} ")
    
            

is_prime(13)
