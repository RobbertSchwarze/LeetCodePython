# Day 49
# Difficulty: 5.5 / 10

# Task:
# Return how many numbers are on the same side of both neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is greater than both neighbors
# - or it is smaller than both neighbors

# Function name:
# count_same_side_neighbors

def count_same_side_neighbors(nums: list[int]) -> int:
    
    # Has to be greater than both neighbors. or smaller than both neighbors.

    count = 0 

    for i in range(1, len(nums) - 1):

        if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]):
            count += 1
        
        if (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]):
            count += 1
    
    return count

print(count_same_side_neighbors([1, 3, 2]))        # 1
print(count_same_side_neighbors([3, 1, 2]))        # 1
print(count_same_side_neighbors([1, 2, 3]))        # 0

# Edge Cases:
print(count_same_side_neighbors([]))               # 0
print(count_same_side_neighbors([1]))              # 0
print(count_same_side_neighbors([1, 2]))           # 0
print(count_same_side_neighbors([1, 1, 1]))        # 0
print(count_same_side_neighbors([1, 2, 1]))        # 1
print(count_same_side_neighbors([3, 2, 4, 1, 5]))  # 3
print(count_same_side_neighbors([5, 3, 4, 2, 1]))  # 2