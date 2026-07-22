# Day 59
# Difficulty: 6 / 10

# Task:
# Return how many numbers are negative while both neighbors are positive.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - current number is negative
# - both neighbors are positive

# Function name:
# count_negative_between_positives

def count_negative_between_positives(nums: list[int]) -> int:

    count = 0

    for i in range(1, len(nums) - 1):

        left_positive = nums[i - 1] > 0
        right_positive = nums[i + 1] > 0
        middle_negative = nums[i] < 0

        if (left_positive and right_positive and middle_negative):
            count += 1

    return count

print(count_negative_between_positives([1, -2, 3]))          # 1
print(count_negative_between_positives([1, -2, 3, -4, 5]))   # 2
print(count_negative_between_positives([-1, -2, -3]))        # 0

# Edge Cases:
print(count_negative_between_positives([]))                  # 0
print(count_negative_between_positives([1]))                 # 0
print(count_negative_between_positives([1, -2]))             # 0
print(count_negative_between_positives([1, 0, 1]))           # 0
print(count_negative_between_positives([5, -1, 2, 3, -4]))   # 1
print(count_negative_between_positives([2, -3, 4, -5, 6]))   # 2