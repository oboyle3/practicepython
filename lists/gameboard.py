size  = 4
def printpipe(num):
    pipe = "|   "
    for z in range(num):
        print(pipe, end = "")
        #print pipe pipe pipe     
#I want to make a 3 x 3 game board
def printdash(num):
    dash = " ---"
    for z in range(num):
        print(dash, end = "")
for x in range(size):
    printdash(size)
    print()
    printpipe(size)
    print()
