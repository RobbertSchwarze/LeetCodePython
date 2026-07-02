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

# Function name:
# count_middle_balanced

def count_middle_balanced(nums: list[int]) -> int:
    
    count = 0

    # So I think what they mean is, we have to find the average, so I will be doing a triple comparison.
    # Then I'll be doing a function. Where I'll get the average so ( 1 + 4) / 2 has to equal the middle number.

    for i in range(1, len(nums) - 1):

        # We'll do the calc

        middle_balanced = (nums[i - 1] + nums[ i + 1]) / 2

        if (middle_balanced == nums[i]):
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