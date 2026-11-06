# Day 63
# Difficulty: 6.5 / 10

# Task:
# Return the length of the longest consecutive section
# where odd and even numbers alternate.

# Definition:
# A section is alternating when:
# - an odd number is followed by an even number
# - or an even number is followed by an odd number
# - two consecutive odd or even numbers break the section

# The length counts how many numbers are in the section.
# An empty list returns 0.
# A single number has a length of 1.

# Function name:
# longest_alternating_parity_streak
def longest_alternating_parity_streak(nums: list[int]) -> int:

    longest_streak = 1
    current_streak = 1

    # An empty list returns 0.
    if (len(nums) == 0): return 0

    for i in range(0, len(nums) - 1):

        # If an odd number is followed by an even number, or if an even number is followed by an odd number we count the streak.
        # odd
        if (nums[i] % 2 == 1 and nums[i+1] % 2 == 0 or nums[i] % 2 == 0 and nums[i+1] % 2 == 1):        
            current_streak += 1
        else:
            current_streak = 1

    # If the current streak is longer than the recorded longest_streak
    # The current streak becomes the longest streak
    if (longest_streak < current_streak):
        longest_streak = current_streak

    return longest_streak


print(longest_alternating_parity_streak([1, 2, 3, 4]))        # 4
print(longest_alternating_parity_streak([2, 4, 6]))           # 1
print(longest_alternating_parity_streak([1, 2, 4, 3, 6]))     # 3

# Edge Cases:
print(longest_alternating_parity_streak([]))                  # 0
print(longest_alternating_parity_streak([7]))                 # 1
print(longest_alternating_parity_streak([1, 3, 5]))           # 1
print(longest_alternating_parity_streak([2, 3, 4, 5]))        # 4
print(longest_alternating_parity_streak([1, 1, 2, 3]))        # 3
print(longest_alternating_parity_streak([2, 3, 4, 4, 5, 6]))  # 3
print(longest_alternating_parity_streak([0, -1, 2, -3]))      # 4