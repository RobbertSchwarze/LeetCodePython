# Day 47
# Difficulty: 5.5 / 10

# Task:
# Return how many numbers are between their two neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is greater than one neighbor
# - and smaller than the other neighbor

# Function name:
# count_between_neighbors

def count_between_neighbors(nums: list[int]) -> int:
    
    count = 0

    for i in range(1, len(nums) - 1):

        if (nums[i] > nums[i + 1] and nums[i] < nums[i - 1]):
            count += 1
        elif(nums[i] < nums[i + 1] and nums[i] > nums[i - 1]):
            count += 1
    
    return count

print(count_between_neighbors([1, 2, 3]))        # 1
print(count_between_neighbors([3, 2, 1]))        # 1
print(count_between_neighbors([1, 3, 2]))        # 0

# Edge Cases:
print(count_between_neighbors([]))               # 0
print(count_between_neighbors([1]))              # 0
print(count_between_neighbors([1, 2]))           # 0
print(count_between_neighbors([1, 1, 1]))        # 0
print(count_between_neighbors([1, 2, 1]))        # 0
print(count_between_neighbors([3, 2, 4, 1, 5]))  # 2
print(count_between_neighbors([5, 3, 4, 2, 1]))  # 2