# Day 62
# Difficulty: 6.5 / 10

# Task:
# Return the length of the longest strictly increasing
# consecutive section in a list.

# Definition:
# A section is strictly increasing when:
# - each number is greater than the previous number
# - the numbers are next to each other in the list
# - equal or decreasing values break the section

# The length counts how many numbers are in the section.
# An empty list returns 0.
# A single number has a length of 1.

# Function name:
# longest_increasing_streak

def longest_increasing_streak(nums: list[int]) -> int:
    longest_streak = 1
    current_streak = 1

    if (len(nums) == 0):
        return 0

    for i in range (1, len(nums)):
        # Each number is greater than the previous number.
        if (nums[i] > nums[i - 1]):
            current_streak += 1
        # Equal or decreasing values break the section
        if (nums[i] == nums[i-1] or nums[i] < nums[i - 1]):
            current_streak = 1

    # If the current streak is bigger than the longest streak.
    # The current streak becomes the longest streak.
        if (current_streak > longest_streak):
            longest_streak = current_streak

    return longest_streak

print(longest_increasing_streak([1, 2, 3, 1, 2]))       # 3
print(longest_increasing_streak([4, 3, 2]))             # 1
print(longest_increasing_streak([1, 2, 2, 3, 4]))       # 3

# Edge Cases:
print(longest_increasing_streak([]))                    # 0
print(longest_increasing_streak([7]))                   # 1
print(longest_increasing_streak([3, 3, 3]))             # 1
print(longest_increasing_streak([5, 6, 7, 8]))          # 4
print(longest_increasing_streak([1, 3, 2, 4, 5, 6, 1])) # 4
print(longest_increasing_streak([1, 2, 1, 2, 3]))       # 3
print(longest_increasing_streak([-3, -2, -1, -4]))      # 3

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern: Streak Tracking