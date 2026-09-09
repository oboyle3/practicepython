# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or exactly right
import random
random_num = random.randint(1,10)
print(f"the random number genrated is {random_num}")
print("")

user_trys = 0
status = True
while status:
    guess = int(input (" enter a ransom num between 1 and 10 "))
    current_guess = guess
    if current_guess < random_num:
        print(f"your guess is to low man")
        print(f" do you want to try again? enter y for yes and n to quit")
        play_again = input()
        if play_again == "y":
            status = True
            user_trys = user_trys + 1
            print("ok lets try again")
    elif current_guess > random_num:
        print(f"your guess is to high man")
        print(f" do you want to try again? enter y for yes and n to quit")
        play_again = input()
        if play_again == "y":
                status = False
                print("lets quit")
    elif current_guess == random_num:
        print(f"you guessed right as the random num was {random_num} and your guess was {guess}")
        status = False