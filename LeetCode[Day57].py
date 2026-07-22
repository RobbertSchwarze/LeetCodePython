# Day 57
# Difficulty: 6 / 10

# Task:
# Return how many numbers are smaller than exactly one neighbor.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is smaller than the number before it OR smaller than the number after it
# - but not both

# Function name:
# count_smaller_than_exactly_one_neighbor

def count_smaller_than_exactly_one_neighbor(nums: list[int]) -> int:

    count = 0

    for i in range(1, len(nums) - 1):

        # Smaller
        left_smaller = nums[i] < nums[i - 1]
        right_smaller = nums[i] < nums[i + 1]

        if (left_smaller != right_smaller):
            count += 1

    return count

print(count_smaller_than_exactly_one_neighbor([1, 2, 3]))        # 1
print(count_smaller_than_exactly_one_neighbor([3, 2, 1]))        # 1
print(count_smaller_than_exactly_one_neighbor([1, 3, 2]))        # 0

# Edge Cases:
print(count_smaller_than_exactly_one_neighbor([]))               # 0
print(count_smaller_than_exactly_one_neighbor([1]))              # 0
print(count_smaller_than_exactly_one_neighbor([1, 2]))           # 0
print(count_smaller_than_exactly_one_neighbor([1, 1, 1]))        # 0
print(count_smaller_than_exactly_one_neighbor([1, 2, 1]))        # 0
print(count_smaller_than_exactly_one_neighbor([2, 1, 3, 2]))     # 0
print(count_smaller_than_exactly_one_neighbor([5, 3, 4, 2, 1]))  # 1

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Triple Comparison, Neighbor Comparison, Counting, Boolean Logic