# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they
# have a “cow”. For every digit the user guessed correctly in the wrong place 
# is a “bull.” Every time the user makes a guess, tell them how many “cows” 
# and “bulls” they have. Once the user guesses the correct number, the game
# is over. Keep track of the number of guesses the user makes throughout the 
# game and tell the user at the end.
import random
import time
# random_num = random.randint(1000,10000)
# print(f"the random num = {random_num} ")
# print(f"guess that random number..")
# user_guess = int(input())
# print("loading..")
# time.sleep(.3)
# print(f"your guess is {user_guess}")
# guess_True_is_still_true = True
# while guess_True_is_still_true:
#     user_guess = user_guess
#     if (user_guess == random_num):
#         print("you win on the first try!")
#         break

#functon takes the guess and returns if one of the digits is right
#can check by puttin into array
def is_right_checker(user_guess, rand_int):
    rand_int_arr = list(str(rand_int))    # 1002
    print(f"rand_int_arr = {rand_int_arr}")
    user_guess_arr = list(str(user_guess))  #1003
    print(f"user_guess_arr = {user_guess_arr}")
    for x in rand_int_arr:
        # print(f"{x} =x")
        print(f"iteration {x} ")
        time.sleep(1)
        if x in user_guess_arr:
            print(f"{x} :  one of your numbers is right!!  ")
        else:
            print(f"lets keep going, and try that again..")
            print("loading")
            time.sleep(3)
            break

randint = 51
# user_guess = 78
the_gamer_wants_to_still_play = True
while the_gamer_wants_to_still_play:
    print("Make a Guess")
    user_guess = int(input())
    print(f"your current guess = {user_guess}")
    if(user_guess == randint):
        print("You Won!")
        the_gamer_wants_to_still_play = False
    else:
        is_right_checker(user_guess,randint)




# is_right_checker(user_guess,randint)

