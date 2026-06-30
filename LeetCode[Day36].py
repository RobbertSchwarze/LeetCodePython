# Day 36
# Difficulty: 4.5 / 10

# Task:
# Return how many times a number is greater than the previous number.

# Examples:
# [1, 2, 3] -> 2
# [3, 2, 1] -> 0
# [1, 1, 2, 2, 3] -> 2

# Edge Cases:
# [] -> 0
# [1] -> 0
# [1, 1] -> 0
# [1, 2] -> 1
# [2, 1] -> 0
# [1, 3, 2, 4] -> 2


def count_increases(nums: list[int]) -> int:
    
    count = 0

    for i in range (0, len(nums) - 1):

        # Alright, so if the number is bigger than the previous number, we need to add +1 to our counter.
        if ( (nums[i] < nums[i+1]) ):
            # We add the counter here.
            count += 1
    
    # After that we'll return our counter.

    return count


print(count_increases([1, 2, 3]))        # 2
print(count_increases([3, 2, 1]))        # 0
print(count_increases([1, 1, 2, 2, 3]))  # 2

print(count_increases([]))               # 0
print(count_increases([1]))              # 0
print(count_increases([1, 1]))           # 0
print(count_increases([1, 2]))           # 1
print(count_increases([2, 1]))           # 0
print(count_increases([1, 3, 2, 4]))     # 2

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison, Counting