# Write a program (using functions!) that asks the user for a long string containing multiple words.
#  Print back to the user the same string, except with the words in backwards order. 
user_str = "Patrick likes tottenham hotspur"
#get each word in the varibe
words = user_str.split()
print(f"the words in array we fetched {words}")
#print words array bawkwards
new_reversed = words[::-1]
print("-----")
print(f"the new reversed array = {new_reversed}")
