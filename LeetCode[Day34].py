# Day 34
# Difficulty: 4 / 10

# Task:
# Return how many times a number is repeated directly.

# Examples:
# [1,1,2,2,2,3] -> 3
# [1,2,3] -> 0
# [5,5,5,5] -> 3

# Edge Cases:
# [] -> 0
# [1] -> 0
# [1,1] -> 1
# [1,1,1] -> 2
# [1,2,2,3,3,3] -> 3
# [1,2,3,4,5] -> 0


def countAdjacentDuplicates(nums: list[int]) -> int:

    duplicates = 0

    for i in range(0, len(nums) - 1):
        # We just have to see if we're how many times a number is repeated directly
        if ( (nums[i] == nums[i + 1]) ):
            #print(f"Duplication detected!")
            # We'll count
            duplicates += 1
    
    # We'll return the duplicates that we have counted so far
    return duplicates

print(countAdjacentDuplicates([1,1,2,2,2,3]))  # 3
print(countAdjacentDuplicates([1,2,3]))        # 0
print(countAdjacentDuplicates([5,5,5,5]))      # 3

print(countAdjacentDuplicates([]))             # 0
print(countAdjacentDuplicates([1]))            # 0
print(countAdjacentDuplicates([1,1]))          # 1
print(countAdjacentDuplicates([1,1,1]))        # 2
print(countAdjacentDuplicates([1,2,2,3,3,3])) # 3
print(countAdjacentDuplicates([1,2,3,4,5]))   # 0


# Time Complexity =
# Space Complexity =
# Pattern =