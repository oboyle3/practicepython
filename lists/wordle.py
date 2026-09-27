import random
avail_words = ["beach"]
rand_word = "beach"

keep_play = True
while keep_play:
    curr_choice = str(input (" enter a word:"))
    if curr_choice == rand_word:
        print("user wins")
        keep_play = False
    else:
        #check rand_word[0] vs curr_choice[0]
        if(rand_word[0] == curr_choice[0]):
            print(f"First letter correct:  {curr_choice[0]}")
        #check rand_word[1] vs curr_choice[2]
        elif(rand_word[1] == curr_choice[1]):
            print(f"First letter correct:  {curr_choice[1]}")
        elif(rand_word[2] == curr_choice[2]):
            print(f"First letter correct:  {curr_choice[2]}")
        elif(rand_word[3] == curr_choice[3]):
            print(f"First letter correct:  {curr_choice[3]}")
        elif(rand_word[4] == curr_choice[4]):
            print(f"First letter correct:  {curr_choice[4]}")
        else:
            print("Nothing found!")
        


