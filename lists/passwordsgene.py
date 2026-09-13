# Write a password generator in Python. Be creative with how you generate
#  passwords - strong passwords have a mix of lowercase letters,
#  uppercase letters, numbers, and symbols. The passwords should 
#  be random, generating a new password every time the user asks for a new password
import random , string
#thinking genrate some random numbers special characters and numbers
#generate random 3 letter num
rand_num1 = random.randint(1,500)
rand_num2 = random.randint(1,500)
rand_num3 = random.randint(1,500)
#genrate random letters
rand_letter1 = random.choice(string.ascii_lowercase)
print(f"rand_letter = {rand_letter1}")
rand_letter2 = random.choice(string.ascii_lowercase)
print(f"rand_letter = {rand_letter2}")
rand_letter3 = random.choice(string.ascii_lowercase)
print(f"rand_letter = {rand_letter3}")
#generate randome symbol
# endoutput = str(rand_num1 + rand_letter1)