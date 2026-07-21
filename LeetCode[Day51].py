# Day 51
# Difficulty: 6 / 10

# Task:
# Return how many numbers are strictly decreasing with their neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - previous > current > next

# Function name:
# count_strictly_decreasing_middle

def count_strictly_decreasing_middle1(nums: list[int]) -> int:

    # Okay so we have to check if the number before, bigger. number after, smaller.
    count = 0

    for i in range(1, len(nums) - 1):

        if (nums[i] < nums[i -1] and nums[i] > nums[i + 1]):
            count += 1

    return count

# I saw that it's better to triple comparison immediatly. 

def count_strictly_decreasing_middle(nums: list[int]) -> int:

    # Okay so we have to check if the number before, bigger. number after, smaller.
    count = 0

    for i in range(1, len(nums) - 1):

        if (nums[i -1 ] > nums[i] > nums[i + 1]):
            count += 1

    return count



print(count_strictly_decreasing_middle([3, 2, 1]))        # 1
print(count_strictly_decreasing_middle([1, 3, 2]))        # 0
print(count_strictly_decreasing_middle([8, 6, 4, 2]))     # 2

# Edge Cases:
print(count_strictly_decreasing_middle([]))               # 0
print(count_strictly_decreasing_middle([1]))              # 0
print(count_strictly_decreasing_middle([1, 2]))           # 0
print(count_strictly_decreasing_middle([3, 3, 2]))        # 0
print(count_strictly_decreasing_middle([3, 2, 2]))        # 0
print(count_strictly_decreasing_middle([1, 2, 3]))        # 0
print(count_strictly_decreasing_middle([5, 4, 3, 4, 2]))  # 1