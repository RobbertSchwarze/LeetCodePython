# Day 64
# Difficulty: 6.5 / 10

# Task:
# Return how many numbers set a new record high
# while moving through the list from left to right.

# Definition:
# A number counts when:
# - it is greater than EVERY number before it
# - equal values do not count as a new record
# - the first number always counts as a record

# An empty list returns 0.

# Function name:
# count_record_highs
def count_record_highs(nums: list[int]) -> int:

    # An empty list returns 0.
    if (len(nums) == 0):
        return 0

    #The first number always counts as record. 
    record_highs = 1
    #We should keep track of the highest_number
    highest_number = nums[0]

    # Just trying to practice with different for loop syntax
    for i in range(0, len(nums) - 1 ):
        # If the highest_number is smaller than the next one, we count a record_high.
        if (highest_number < nums[i + 1]):
            record_highs += 1
            # We have to reset the highest_number, to the next number.
            highest_number = nums [i + 1]

    return record_highs

print(count_record_highs([3, 1, 4, 2, 5]))      # 3
print(count_record_highs([5, 4, 3, 2]))         # 1
print(count_record_highs([1, 2, 3, 4]))         # 4

# Edge Cases:
print(count_record_highs([]))                  # 0
print(count_record_highs([7]))                 # 1
print(count_record_highs([3, 3, 3]))           # 1
print(count_record_highs([1, 1, 2, 2, 3]))     # 3
print(count_record_highs([-5, -3, -4, -1]))    # 3
print(count_record_highs([2, 1, 2, 3]))        # 2
print(count_record_highs([0, -1, -2]))         # 1
print(count_record_highs([1, 3, 2, 4, 5]))     # 4