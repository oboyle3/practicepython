#how to keep playing and make sure word is 5 letters
import random
avail_words = [
    "apple",
    "house",
    "plant",
    "chair",
    "table",
    "water",
    "green",
    "black",
    "white",
    "world",
    "light",
    "sound",
    "music",
    "river",
    "ocean",
    "beach",
    "cloud",
    "storm",
    "grass",
    "stone",
    "bread",
    "money",
    "phone",
    "train",
    "plane",
    "truck",
    "horse",
    "sheep",
    "tiger",
    "eagle",
    "mouse",
    "snake",
    "grape",
    "peach",
    "lemon",
    "berry",
    "pizza",
    "pasta",
    "sugar",
    "sweet",
    "happy",
    "smile",
    "laugh",
    "dream",
    "sleep",
    "think",
    "learn",
    "write",
    "read",
    "study"
]
rand_word = random.choice(avail_words)
keep_play = True
print(rand_word)
while keep_play:
    curr_choice = str(input (" enter a 5 letter word:"))
    if len(curr_choice) > 5:
           print("Word must be 5 letters | you entered to many letters")
           #keep_play = True
    elif len(curr_choice) < 5:
          print("Word must be 5 letters | you entered to less letters")
    elif len(curr_choice) == 5:
        if curr_choice == rand_word:
                    print(f"user wins | ")
                    keep_play = False
       #check rand_word[0] vs curr_choice[0]
        if(rand_word[0] == curr_choice[0]):
            print(f"First letter correct:     {curr_choice[0]}")
                  #check rand_word[1] vs curr_choice[2]
        if(rand_word[1] == curr_choice[1]):
                      print(f"Second letter correct:    {curr_choice[1]}")
        if(rand_word[2] == curr_choice[2]):
                      print(f"Third letter correct:     {curr_choice[2]}")
        if(rand_word[3] == curr_choice[3]):
                      print(f"Fourth letter correct:     {curr_choice[3]}")
        if(rand_word[4] == curr_choice[4]):
                      print(f"Fith letter correct:    {curr_choice[4]}")
                  