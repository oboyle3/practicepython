rock = "rock"
paper = "paper"
siz = "siz"
#simulate choice1 and choice2
choice1 = rock
choice2 = siz
if choice1 == rock and choice2 == paper:
    print("paper wins")
elif choice1 == rock and choice2 == siz:
    print("rock wins")
elif choice1 == siz and choice2 == rock:
    print("rock wins")
elif choice1 == siz and choice2 == paper:
    print("siz wins")
elif choice1 == paper and choice2 == rock:
    print("paper wins")
elif choice1 == paper and choice2 == rock:
    print("paper wins")
else: print("invalid")
