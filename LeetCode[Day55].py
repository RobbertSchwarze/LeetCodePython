# Day 55
# Difficulty: 6 / 10

# Task:
# Return how many numbers are equal to neither neighbor.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is not equal to the number before it
# - and it is not equal to the number after it

# Function name:
# count_equal_to_neither_neighbor

def count_equal_to_neither_neighbor(nums: list[int]) -> int:

    count = 0

    for i in range(1, len(nums) - 1):

        left_is_different = nums[i - 1] != nums[i]
        right_is_different = nums[i + 1] != nums[i]

        if (left_is_different and right_is_different):
            count += 1
        
    return count

print(count_equal_to_neither_neighbor([1, 2, 1]))        # 1
print(count_equal_to_neither_neighbor([1, 1, 1]))        # 0
print(count_equal_to_neither_neighbor([1, 2, 2, 3]))     # 0

# Edge Cases:
print(count_equal_to_neither_neighbor([]))               # 0
print(count_equal_to_neither_neighbor([1]))              # 0
print(count_equal_to_neither_neighbor([1, 2]))           # 0
print(count_equal_to_neither_neighbor([1, 2, 3]))        # 1
print(count_equal_to_neither_neighbor([2, 2, 3, 2]))     # 1
print(count_equal_to_neither_neighbor([5, 5, 4, 4, 4]))  # 0
print(count_equal_to_neither_neighbor([1, 2, 1, 3, 1]))  # 3

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison, Triple Comparison, Counting, Boolean Logic