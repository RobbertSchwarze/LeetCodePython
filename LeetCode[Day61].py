# Day 61
# Difficulty: 6 / 10

# Task:
# Return how many numbers have neighbors with the same sign.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - both neighbors are positive
# - or both neighbors are negative
# - zero is neither positive nor negative

# Function name:
# count_between_same_sign_neighbors
def count_between_same_sign_neighbors(nums: list[int]) -> int:

    count = 0

    for i in range(1, len(nums) - 1):

        left_positive = nums[i + 1] > 0
        left_negative = nums[i - 1] < 0

        right_positive = nums[i - 1] > 0
        right_negative = nums[i + 1] < 0

        if ( (left_positive and right_positive) or (left_negative and right_negative) ):
            count += 1

    return count

print(count_between_same_sign_neighbors([1, 5, 2]))           # 1
print(count_between_same_sign_neighbors([-1, 5, -2]))         # 1
print(count_between_same_sign_neighbors([-1, 5, 2]))          # 0

# Edge Cases:
print(count_between_same_sign_neighbors([]))                  # 0
print(count_between_same_sign_neighbors([1]))                 # 0
print(count_between_same_sign_neighbors([1, 2]))              # 0
print(count_between_same_sign_neighbors([-1, 0, -1]))         # 1
print(count_between_same_sign_neighbors([1, 0, 1]))           # 1
print(count_between_same_sign_neighbors([1, 0, 0]))           # 0
print(count_between_same_sign_neighbors([-2, 4, -3, -5, 6]))  # 1

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison, Triple Comparison, Boolean Logic, Counting