# Day 41
# Difficulty: 5 / 10

# Task:
# Return how many numbers are "middle-balanced".

# A number is middle-balanced when:
# - it has a number before it
# - it has a number after it
# - and it is exactly between them

# Examples:
# [1, 2, 3] -> 1
# [2, 4, 6, 5] -> 1
# [1, 3, 2] -> 0

# Edge Cases:
# [] -> 0
# [1] -> 0
# [1, 2] -> 0
# [1, 2, 3] -> 1
# [3, 2, 1] -> 1
# [1, 2, 4] -> 0
# [2, 4, 6, 8, 10] -> 3
# [1, 3, 5, 4, 3] -> 2

def count_middle_balanced(nums: list[int]) -> int:
    
    count = 0

    for i in range(1, len(nums) - 1):

        neighbor_average = (nums[i - 1] + nums[i + 1]) / 2

        if (neighbor_average == nums[i]):
            count += 1
    
    return count
         

print(count_middle_balanced([1, 2, 3]))          # 1
print(count_middle_balanced([2, 4, 6, 5]))       # 1
print(count_middle_balanced([1, 3, 2]))          # 0

print(count_middle_balanced([]))                 # 0
print(count_middle_balanced([1]))                # 0
print(count_middle_balanced([1, 2]))             # 0
print(count_middle_balanced([1, 2, 3]))          # 1
print(count_middle_balanced([3, 2, 1]))          # 1
print(count_middle_balanced([1, 2, 4]))          # 0
print(count_middle_balanced([2, 4, 6, 8, 10]))   # 3
print(count_middle_balanced([1, 3, 5, 4, 3]))    # 2

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Comparison, Triple Comparison, Counting