# Day 58
# Difficulty: 6 / 10

# Task:
# Return how many numbers are positive while both neighbors are negative.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - current number is positive
# - both neighbors are negative

# Function name:
# count_positive_between_negatives

def count_positive_between_negatives(nums: list[int]) -> int:

    count = 0

    for i in range(1, len(nums) - 1):

        # Let'see.
        # Both numbers next i have to be negative.
        # And the number we're checking have to be positive.

        left_negative = nums[i - 1] < 0
        right_negative = nums[i + 1] < 0
        middle_positive = nums[i] > 0

        if (left_negative and right_negative and middle_positive):
            count += 1

    return count


print(count_positive_between_negatives([-1, 2, -3]))          # 1
print(count_positive_between_negatives([-1, 2, -3, 4, -5]))   # 2
print(count_positive_between_negatives([1, 2, 3]))            # 0

# Edge Cases:
print(count_positive_between_negatives([]))                   # 0
print(count_positive_between_negatives([1]))                  # 0
print(count_positive_between_negatives([-1, 2]))              # 0
print(count_positive_between_negatives([-1, -2, -3]))         # 0
print(count_positive_between_negatives([-1, 0, -1]))          # 0
print(count_positive_between_negatives([-5, 1, -2, -3, 4]))   # 1
print(count_positive_between_negatives([-2, 3, -4, 5, -6]))   # 2

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison, Triple Comparison, Boolean Logic, Counting