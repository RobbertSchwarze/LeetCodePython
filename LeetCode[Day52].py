# Day 52
# Difficulty: 6 / 10

# Task:
# Return how many numbers are part of a flat middle.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - previous == current == next

# Function name:
# count_flat_middle

def count_flat_middle(nums: list[int]) -> int:
    count = 0

    for i in range(1, len(nums) - 1):
        
        if (nums[i - 1] == nums[i] == nums[i + 1]):
            count += 1

    return count 

print(count_flat_middle([1, 1, 1]))        # 1
print(count_flat_middle([2, 2, 2, 2]))     # 2
print(count_flat_middle([1, 2, 2, 2, 3]))  # 1

# Edge Cases:
print(count_flat_middle([]))               # 0
print(count_flat_middle([1]))              # 0
print(count_flat_middle([1, 1]))           # 0
print(count_flat_middle([1, 2, 1]))        # 0
print(count_flat_middle([3, 3, 2, 3, 3]))  # 0
print(count_flat_middle([5, 5, 5, 5, 5]))  # 3
