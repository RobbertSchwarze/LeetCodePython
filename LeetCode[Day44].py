# Day 44
# Difficulty: 5.5 / 10

# Task:
# Return how many numbers are different from both of their neighbors.

# Definition:
# A number counts when:
# - it has a number before it
# - it has a number after it
# - it is not equal to the number before it
# - it is not equal to the number after it

# Function name:
# count_different_from_neighbors

def count_different_from_neighbors(nums: list[int]) -> int:

    # Alright, pretty simple. It has to have neighbors, which is given with the code i'll be writing.
    # I feel like it's just a != to the number before and after it.

    count = 0

    for i in range(1, len(nums) - 1):
        if (nums[i] != nums[i - 1] and nums[i] != nums[i + 1]):
            count += 1

    return count

print(count_different_from_neighbors([1, 2, 1]))        # 1
print(count_different_from_neighbors([1, 2, 3]))        # 1
print(count_different_from_neighbors([1, 1, 2, 1]))     # 1

# Edge Cases:
print(count_different_from_neighbors([]))               # 0
print(count_different_from_neighbors([1]))              # 0
print(count_different_from_neighbors([1, 2]))           # 0
print(count_different_from_neighbors([1, 1, 1]))        # 0
print(count_different_from_neighbors([1, 2, 2, 1]))     # 0
print(count_different_from_neighbors([1, 2, 1, 2, 1]))  # 3
print(count_different_from_neighbors([3, 3, 2, 4, 4]))  # 1

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison, Triple Comparison, Counting