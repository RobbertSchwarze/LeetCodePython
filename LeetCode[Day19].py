# Return hoeveel paren (i, j) bestaan waarbij:
# i < j
# nums[i] == nums[j]

# Voorbeeld:
# [1,2,1,1] -> 3

def countEqualsPairs(nums: list[int]) -> int:

    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] == nums[j]):
                count += 1
    
    return count

print(countEqualsPairs([1,2,1,1]))

# Space Complexity = O(1)
# Time Complexity = O(n^2)
# counting, Pair Comparison


    