# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or exactly right
import random
random_num = random.randint(1,10)
print(f"the random number genrated is {random_num}")
print("")
guess = int(input (" enter a ransom num between 1 and 10 "))
print(f"you guessed {guess}")
status = True
if guess < random_num:
    print(f"your guess is to low man")
elif guess > random_num:
    print(f"your guess is to high man")
elif guess == random_num:
    print(f"you guessed right as the random num was {random_num} and your guess was {guess}")