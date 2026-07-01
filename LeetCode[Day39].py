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
    # If the following number is bigger then the one before it and the one after it.
    # It's a peak !

    count = 0

    for i in range(0, len(nums) - 2):
        if (nums[i] < nums[i + 1] and nums[i + 1] > nums [i + 2]):
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