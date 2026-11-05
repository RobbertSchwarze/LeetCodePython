# Day 63
# Difficulty: 6.5 / 10

# Task:
# Return the length of the longest strictly decreasing
# consecutive section in a list.

# Definition:
# A section is strictly decreasing when:
# - each number is smaller than the previous number
# - the numbers are next to each other in the list
# - equal or increasing values break the section

# The length counts how many numbers are in the section.
# An empty list returns 0.
# A single number has a length of 1.

# Function name:
# longest_decreasing_streak
def longest_decreasing_streak (nums: list[int]) -> int:
    
    longest_streak = 1
    current_streak = 1

    if (len(nums) == 0):
        return 0

    for i in range(1, len(nums)):

        # Each number is smaller than the previous number
        if (nums[i] < nums[i -1]):
            current_streak += 1
            # Equal or increasing break the section
        else:
            current_streak = 1

        # If the current_streak is bigger then the longest streak
        # The longest streak becomes the current streak
        if (current_streak > longest_streak):
            longest_streak = current_streak
    
    return longest_streak


print(longest_decreasing_streak([5, 4, 3, 7, 6]))       # 3
print(longest_decreasing_streak([1, 2, 3]))             # 1
print(longest_decreasing_streak([9, 7, 7, 6, 5]))       # 3

# Edge Cases:
print(longest_decreasing_streak([]))                    # 0
print(longest_decreasing_streak([7]))                   # 1
print(longest_decreasing_streak([3, 3, 3]))             # 1
print(longest_decreasing_streak([5, 4, 3, 2]))          # 4
print(longest_decreasing_streak([3, 2, 5, 4, 1]))       # 3
print(longest_decreasing_streak([5, 5, 4, 3, 2, 6]))    # 4
print(longest_decreasing_streak([-1, -2, -3, 0, -1]))   # 3