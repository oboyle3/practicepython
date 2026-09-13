# Write a password generator in Python. Be creative with how you generate
#  passwords - strong passwords have a mix of lowercase letters,
#  uppercase letters, numbers, and symbols. The passwords should 
#  be random, generating a new password every time the user asks for a new password
import random , string


def give_pw():
    rand_num1 = random.randint(1,500)
    RANDOM_NUMBER1 = str(rand_num1)
    rand_num2 = random.randint(1,500)
    RANDOM_NUMBER2 = str(rand_num2)
    rand_num3 = random.randint(1,500)
    RANDOM_NUMBER3 = str(rand_num3)
    #genrate random letters
    rand_letter1upercase = random.choice(string.ascii_uppercase)
    rand_letter1 = random.choice(string.ascii_lowercase)
    print(f"rand_letter = {rand_letter1}")
    rand_letter2 = random.choice(string.ascii_lowercase)
    print(f"rand_letter = {rand_letter2}")
    rand_letter3 = random.choice(string.ascii_lowercase)
    print(f"rand_letter = {rand_letter3}")
    print(f"RANDOM_NUMBER1 = {RANDOM_NUMBER1}")
    print(f"RANDOM_NUMBER2 = {RANDOM_NUMBER2}")
    print(f"RANDOM_NUMBER3 = {RANDOM_NUMBER3}")
    #generate randome symbol
    final_pw = rand_letter1upercase +RANDOM_NUMBER2 + rand_letter1+ RANDOM_NUMBER3 + rand_letter2 + rand_letter3 + RANDOM_NUMBER1 
    print(f" final pw the user can use: {final_pw}")

give_pw()



