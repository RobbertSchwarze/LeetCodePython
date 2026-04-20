# Day 2 Array (LISTS) + loop

# Task
# Write a function what returns the sum of all numbers.
# Examples:
# [1, 2, 3] -> 6
# [5] -> 5
# [] -> 0

# Make a list
# Declare a sum to return
# Walk through the list
# sum += the array[0]
# return the sum

nums = [1, 2, 3]

def sum_list(nums: list[int]) -> int:
    sum = 0

    for num in nums:
        sum += num
    
    return sum

print(sum_list(nums))