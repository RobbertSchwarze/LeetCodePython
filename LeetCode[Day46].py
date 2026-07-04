# Day 46
# Difficulty: 5.5 / 10

# Task:
# Return how many numbers are equal to both of their neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is equal to the number before it
# - and it is equal to the number after it

# Function name:
# count_equal_to_both_neighbors

def count_equal_to_both_neighbors(nums: list[int]) -> int:
    
    count = 0

    for i in range (1, len(nums) - 1):

        if (nums[i] == nums[i - 1] and nums[i] == nums[i + 1]):
            count += 1
   
    return count

print(count_equal_to_both_neighbors([1, 1, 1]))        # 1
print(count_equal_to_both_neighbors([1, 2, 2, 2, 3]))  # 1
print(count_equal_to_both_neighbors([5, 5, 5, 5]))     # 2

# Edge Cases:
print(count_equal_to_both_neighbors([]))               # 0
print(count_equal_to_both_neighbors([1]))              # 0
print(count_equal_to_both_neighbors([1, 1]))           # 0
print(count_equal_to_both_neighbors([1, 2, 1]))        # 0
print(count_equal_to_both_neighbors([2, 2, 3, 2, 2]))  # 0
print(count_equal_to_both_neighbors([4, 4, 4, 1, 1]))  # 1