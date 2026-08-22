# Character Input 
# input strings types int
# Exercise 1 (and Solution)
# Create a program that asks the user to enter their name and 
# their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
import time
print(f"Character Input")
print(f"Hi please  enter your name...")
name = input()
print(f"Please enter your age...")
age = int(input())
print(f"You entered: name = {name} and your age = {age}")
year = 100
when_they_will_turn_a_hundred = (year - age)
print(f"you will turn 100 years old in...")
time.sleep(.5)
current_year = (2026+ when_they_will_turn_a_hundred)
print(f"{when_they_will_turn_a_hundred} , years...   in ... {current_year}")
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
print(f"enter another number")
num = int(input())
for x in range(num):
    print(f"{when_they_will_turn_a_hundred} , years...   in ... {current_year}")