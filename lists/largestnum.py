numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for x in range(len(numbers)-1):
    current_num = numbers[x]
    next_num = numbers[x+1]
    if current_num > next_num:
        largest = current_num
        print(f"current_num {current_num} < next_num {next_num}")

    print(f"largest = {largest}")
    

    