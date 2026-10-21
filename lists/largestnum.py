numbers = [12, 45, 7, 89, 23]

#Find largest num given arr

largest = numbers[0]
for x in range(2):
    largest = numbers[x]
    print(f"largest = {largest}")
    # largest is 12 lets check the number next to it
    num_to_left = numbers[x+1]
    print(f"num to left = {num_to_left}")
    

    