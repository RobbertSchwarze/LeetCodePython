# Day 66
# Difficulty: 6.5 / 10

# Task:
# Return how many numbers set a new record low
# while moving through the list from left to right.

# Definition:
# A number counts when:
# - it is smaller than EVERY number before it
# - equal values do not count as a new record
# - the first number always counts as a record

# An empty list returns 0.

# Function name:
# count_record_lows
def count_record_lows(nums: list[int]) -> int:

    # An empty list returns 0.
    if (len(nums) == 0):
        return 0

    # First number always counts as a record.
    record_lows = 1
    # If it is smaller than EVERY number before it, we should keep track of the first number.
    smallest_number = nums[0]

    for i in range(0, len(nums) - 1):
        # We count if it is smaller than the number before it.
        if (nums[i + 1] < smallest_number):
            record_lows += 1
            # We also update the lowest number, to the newer lower number.
            smallest_number = nums[i + 1]

    return record_lows


print(count_record_lows([3, 5, 2, 4, 1]))      # 3
print(count_record_lows([1, 2, 3, 4]))         # 1
print(count_record_lows([5, 4, 3, 2]))         # 4

# Edge Cases:
print(count_record_lows([]))                  # 0
print(count_record_lows([7]))                 # 1
print(count_record_lows([3, 3, 3]))           # 1
print(count_record_lows([2, 1, 2, 0]))        # 3
print(count_record_lows([-1, -3, -2, -5]))    # 3
print(count_record_lows([0, 1, -1, -1, -2]))  # 3
print(count_record_lows([5, 1, 4, 0, -1]))    # 4