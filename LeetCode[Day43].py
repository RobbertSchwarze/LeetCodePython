# Day 43
# Difficulty: 5 / 10

# Task:
# Return how many numbers are smaller than both of their neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is smaller than both neighbors

# Function name:
# count_smaller_than_neighbors

def count_smaller_than_neighbors(nums: list[int]) -> int:
    
    count = 0

    for i in range(1, len(nums) - 1):

        if (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]):
            count += 1

    return count

print(count_smaller_than_neighbors([3, 1, 2]))        # 1
print(count_smaller_than_neighbors([1, 2, 3]))        # 0
print(count_smaller_than_neighbors([5, 2, 4, 1, 3]))  # 2

# Edge Cases:
print(count_smaller_than_neighbors([]))               # 0
print(count_smaller_than_neighbors([1]))              # 0
print(count_smaller_than_neighbors([1, 2]))           # 0
print(count_smaller_than_neighbors([1, 1, 1]))        # 0
print(count_smaller_than_neighbors([1, 3, 1]))        # 0
print(count_smaller_than_neighbors([4, 1, 4, 2, 5]))  # 2

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison, Triple Comparison, Counting