# Day 39
# Difficulty: 5 / 10

# Task:
# Return how many "peaks" are in the list.

# A peak means:
# - the number is greater than the number before it
# - and greater than the number after it

# Examples:
# [1, 3, 2] -> 1
# [1, 2, 3] -> 0
# [1, 3, 2, 4, 1] -> 2

# Edge Cases:
# [] -> 0
# [1] -> 0
# [1, 2] -> 0
# [1, 3, 2] -> 1
# [3, 1, 3] -> 0
# [1, 2, 2, 1] -> 0
# [1, 3, 1, 3, 1] -> 2


def count_peaks(nums: list[int]) -> int:
    # We need to detect a peak.
    # A peak happens with three numbers.
    # If the following number is bigger than the one before it and the one after it.
    # It's a peak !

    count = 0

    for i in range(0, len(nums) - 2):
        if (nums[i] < nums[i + 1] and nums[i + 1] > nums[i + 2]):
            # PEAK !
            count += 1
    
    return count

print(count_peaks([1, 3, 2]))           # 1
print(count_peaks([1, 2, 3]))           # 0
print(count_peaks([1, 3, 2, 4, 1]))     # 2

print(count_peaks([]))                  # 0
print(count_peaks([1]))                 # 0
print(count_peaks([1, 2]))              # 0
print(count_peaks([1, 3, 2]))           # 1
print(count_peaks([3, 1, 3]))           # 0
print(count_peaks([1, 2, 2, 1]))        # 0
print(count_peaks([1, 3, 1, 3, 1]))     # 2

# Also another version for readability

def count_peaks_cleaner_code(nums: list[int]) -> int:

    counter = 0 

    # We do this, in order to make i the middle number.
    # For readability this is easier.
    # But same solution, just a bit easier to read.
    for i in range(1, len(nums) - 1):
        if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]):
            counter += 1
    
    return counter
    

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison + Counting + Triple Comparison