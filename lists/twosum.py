# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
nums = [2,7,11,15]
target = 9
nextnum = 0
for x in range(len(nums) - 1):
    current_element = nums[x]
    print(f"current_element = {current_element}")
    next_element = nums[x + 1]
    print(f"next_element = {next_element}")
    sum_of_current_and_next = current_element  + next_element
    print(f"sum = {sum_of_current_and_next}")
    if sum_of_current_and_next == target:
        print("you win")
        break
def twoSum(self, nums, target):
    nextnum = 0
    