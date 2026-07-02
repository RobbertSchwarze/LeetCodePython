# Day 40
# Difficulty: 5 / 10

# Task:
# Return how many "valleys" are in the list.

# A valley means:
# - the number is smaller than the number before it
# - and smaller than the number after it

# Examples:
# [3, 1, 2] -> 1
# [1, 2, 3] -> 0
# [5, 2, 4, 1, 3] -> 2

# Edge Cases:
# [] -> 0
# [1] -> 0
# [1, 2] -> 0
# [3, 1, 2] -> 1
# [1, 3, 1] -> 0
# [2, 2, 1, 2] -> 1
# [3, 1, 3, 1, 3] -> 2


def count_valleys(nums: list[int]) -> int:

    count = 0
    
    for i in range(1, len(nums) - 1):
        if (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]):
            count += 1
    
    return count

print(count_valleys([3, 1, 2]))           # 1
print(count_valleys([1, 2, 3]))           # 0
print(count_valleys([5, 2, 4, 1, 3]))     # 2

print(count_valleys([]))                  # 0
print(count_valleys([1]))                 # 0
print(count_valleys([1, 2]))              # 0
print(count_valleys([3, 1, 2]))           # 1
print(count_valleys([1, 3, 1]))           # 0
print(count_valleys([2, 2, 1, 2]))        # 1
print(count_valleys([3, 1, 3, 1, 3]))     # 2

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison, Counting, Triple Comparison