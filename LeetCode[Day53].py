# Day 53
# Difficulty: 6 / 10

# Task:
# Return how many numbers are NOT equal to both of their neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is not equal to the number before it
# - or it is not equal to the number after it

# Function name:
# count_not_equal_to_both_neighbors

def count_not_equal_to_both_neighbors(nums: list[int]) -> int:

    count = 0

    for i in range(1, len(nums) - 1):
        
        if (nums[i - 1] != nums[i]):
            count += 1
        elif(nums[i + 1] != nums[i]):
            count += 1
    
    return count

print(count_not_equal_to_both_neighbors([1, 2, 1]))        # 1
print(count_not_equal_to_both_neighbors([1, 1, 1]))        # 0
print(count_not_equal_to_both_neighbors([1, 2, 2, 3]))     # 2

# Edge Cases:
print(count_not_equal_to_both_neighbors([]))               # 0
print(count_not_equal_to_both_neighbors([1]))              # 0
print(count_not_equal_to_both_neighbors([1, 2]))           # 0
print(count_not_equal_to_both_neighbors([2, 2, 2]))        # 0
print(count_not_equal_to_both_neighbors([2, 2, 3, 2]))     # 2
print(count_not_equal_to_both_neighbors([1, 2, 3, 4]))     # 2
print(count_not_equal_to_both_neighbors([5, 5, 4, 4, 4]))  # 2