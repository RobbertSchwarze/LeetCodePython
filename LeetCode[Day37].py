# Day 37
# Difficulty: 4.5 / 10

# Task:
# Return how many times a number is smaller than the previous number.

# Examples:
# [3, 2, 1] -> 2
# [1, 2, 3] -> 0
# [5, 5, 4, 4, 3] -> 2

# Edge Cases:
# [] -> 0
# [1] -> 0
# [1, 1] -> 0
# [2, 1] -> 1
# [1, 2] -> 0
# [5, 3, 4, 2, 1] -> 3


def count_decreases(nums: list[int]) -> int:
    
    # Okay so very simple, we need to detect when the a number is smaller than the previous number.
    # Let's set up an integer that's called count
    count = 0

    # We'll walk through the for loop to compare our integers.
    for i in range(0, len(nums) - 1):
        if ( nums[i] > nums[i + 1] ):
            count += 1

    return count


print(count_decreases([3, 2, 1]))        # 2
print(count_decreases([1, 2, 3]))        # 0
print(count_decreases([5, 5, 4, 4, 3]))  # 2

print(count_decreases([]))               # 0
print(count_decreases([1]))              # 0
print(count_decreases([1, 1]))           # 0
print(count_decreases([2, 1]))           # 1
print(count_decreases([1, 2]))           # 0
print(count_decreases([5, 3, 4, 2, 1]))  # 3

# Space Complexity = O(1)
# Time Complexity = O(n)
# Pattern = Neighbor Tracking, Counting