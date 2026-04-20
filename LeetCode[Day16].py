# Opdracht:

# Return de som van alle paren (i, j) waarbij:
# i < j is.

# Voorbeeld [1, 2 ,3]

# (1, 2) = 3
# (1, 3) = 4
# (2, 3) = 5
# Output: 12

def sumOfPairs(nums: list[int]) -> int:

    sum = 0
    total = 0

    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i < j):
                print(f"sum: {nums[i]} + {nums[j]}")
                sum = nums[i] + nums[j]
                total += sum

        
    return total

print(sumOfPairs([1,2,3]))
