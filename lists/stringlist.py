# Ask the user for a string and print out whether this string is a palindrome 
# or not. (A palindrome is a string that reads the same forwards and backwards.)
word = "race"
put_word_in_temp_list = []
# put these in a array then check if the array are the same?
for x in word:
    put_word_in_temp_list.append(x)
print(f"temp list = {put_word_in_temp_list}")
# is the list the same backward and foward?
#just reverse the array and see if they are the same??
temp_list_to_check = []
for y in reversed(put_word_in_temp_list):
    temp_list_to_check.append(y)
print(f"temp list toc check = {temp_list_to_check}")

if put_word_in_temp_list == temp_list_to_check:
    print(f"yes palindrome")
else:
    print("not palindrome")

