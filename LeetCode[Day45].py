# Day 45
# Difficulty: 5.5 / 10

# Task:
# Return how many numbers are equal to at least one of their neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is equal to the number before it
# - or it is equal to the number after it

# Function name:
# count_equal_to_neighbor

def count_equal_to_neighbor(nums: list[int]) -> int:
    
    count = 0

    for i in range(1, len(nums) - 1):

        if (nums[i] == nums[i - 1] or nums[i] == nums[i + 1]):
            count += 1

    return count 

print(count_equal_to_neighbor([1, 2, 2]))        # 1
print(count_equal_to_neighbor([1, 1, 2, 3]))     # 1
print(count_equal_to_neighbor([1, 2, 2, 3, 3]))  # 3

# Edge Cases:
print(count_equal_to_neighbor([]))               # 0
print(count_equal_to_neighbor([1]))              # 0
print(count_equal_to_neighbor([1, 2]))           # 0
print(count_equal_to_neighbor([1, 1, 1]))        # 1
print(count_equal_to_neighbor([1, 2, 3]))        # 0
print(count_equal_to_neighbor([1, 2, 1]))        # 0
print(count_equal_to_neighbor([2, 2, 3, 4, 4]))  # 2

# Space Complexity = O(1)
# Time Complexity = O(n)
# Pattern = Neighbor Comparison, Triple Comparison, Counting 