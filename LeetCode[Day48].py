# Day 48
# Difficulty: 5.5 / 10

# Task:
# Return how many numbers are NOT between their two neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is NOT greater than one neighbor and smaller than the other neighbor
# - equal values do not count as between

# Function name:
# count_not_between_neighbors

def count_not_between_neighbors(nums: list[int]) -> int:

    count = 0
    
    for i in range(1, len(nums) - 1):

        if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]):
            count += 1
        if (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]):
            count+= 1     
        if (nums[i] == nums[i - 1] and nums[i] == nums[i + 1]):
            count+=1
            
    
    return count


print(count_not_between_neighbors([1, 3, 2]))        # 1
print(count_not_between_neighbors([1, 2, 3]))        # 0
print(count_not_between_neighbors([3, 2, 1]))        # 0

# Edge Cases:
print(count_not_between_neighbors([]))               # 0
print(count_not_between_neighbors([1]))              # 0
print(count_not_between_neighbors([1, 2]))           # 0
print(count_not_between_neighbors([1, 1, 1]))        # 1
print(count_not_between_neighbors([1, 2, 1]))        # 1
print(count_not_between_neighbors([3, 2, 4, 1, 5]))  # 3
print(count_not_between_neighbors([5, 3, 4, 2, 1]))  # 2

# Time Complexity = O(n)
# Space Complextiy = O(1)
# Pattern = Neighbor Comparison, Triple Comparison, Counting.