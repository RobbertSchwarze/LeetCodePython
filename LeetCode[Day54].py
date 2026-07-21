# Day 54
# Difficulty: 6 / 10

# Task:
# Return how many numbers are equal to exactly one neighbor.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is equal to the number before it OR equal to the number after it
# - but not both

# Function name:
# count_equal_to_exactly_one_neighbor

def count_equal_to_exactly_one_neighbor(nums: list[int]) -> int:

    count = 0 

    for i in range(1, len(nums) - 1):
        if (nums[i] == nums[i - 1] or nums[i] == nums[i + 1]):
            count += 1
        if (nums[i] == nums[i - 1] and nums[i] == nums[i + 1]):
            count -= 1
    
    return count


print(count_equal_to_exactly_one_neighbor([1, 1, 2]))        # 1
print(count_equal_to_exactly_one_neighbor([1, 1, 1]))        # 0
print(count_equal_to_exactly_one_neighbor([1, 2, 2, 3]))     # 2

# Edge Cases:
print(count_equal_to_exactly_one_neighbor([]))               # 0
print(count_equal_to_exactly_one_neighbor([1]))              # 0
print(count_equal_to_exactly_one_neighbor([1, 2]))           # 0
print(count_equal_to_exactly_one_neighbor([2, 2, 2]))        # 0
print(count_equal_to_exactly_one_neighbor([2, 2, 3, 2]))     # 1
print(count_equal_to_exactly_one_neighbor([1, 2, 3, 4]))     # 0
print(count_equal_to_exactly_one_neighbor([5, 5, 4, 4, 4]))  # 2