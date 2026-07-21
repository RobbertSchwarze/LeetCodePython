# Day 50
# Difficulty: 6 / 10

# Task:
# Return how many numbers are strictly increasing with their neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - previous < current < next

# Function name:
# count_strictly_increasing_middle

def count_strictly_increasing_middle(nums: list[int]) -> int:
    
    # Okay so it has to strictly increase. 
    # We have to return how many numbers are increasing, but we're only counting the middle one.
    count = 0

    for i in range(1, len(nums) - 1):

        if (nums[i] > nums[i - 1] and nums[i] < nums[i + 1]):
            count += 1
    
    return count
    

print(count_strictly_increasing_middle([1, 2, 3]))        # 1
print(count_strictly_increasing_middle([1, 3, 2]))        # 0
print(count_strictly_increasing_middle([2, 4, 6, 8]))     # 2

# Edge Cases:
print(count_strictly_increasing_middle([]))               # 0
print(count_strictly_increasing_middle([1]))              # 0
print(count_strictly_increasing_middle([1, 2]))           # 0
print(count_strictly_increasing_middle([1, 1, 2]))        # 0
print(count_strictly_increasing_middle([1, 2, 2]))        # 0
print(count_strictly_increasing_middle([3, 2, 1]))        # 0
print(count_strictly_increasing_middle([1, 2, 3, 2, 4]))  # 1