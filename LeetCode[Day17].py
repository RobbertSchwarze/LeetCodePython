# Opdracht:

# Return de grootste som van een paar (i, j) waarbij:
# i < j

# Voorbeeld:

# [1,2,3] -> 5(2+3)
# [5,1,4,2] -> 9 (5 + 4)

def maxPairSum(nums: list[int]) -> int:

    maxSum = float("-inf")
    sum = 0

    for i in range(len(nums)):
        for j in range( i + 1, len(nums)):
            # Als i < j dan tellen we de totale waarde op.
            if (i < j):
                sum = ( (nums[i]) + (nums[j]) )
                if ( (nums[i] + nums[j]) > maxSum ):
                    maxSum = sum
    
    return maxSum


print(maxPairSum([1,2,3])) # --> 5 (2 + 3)
print(maxPairSum([5,1,4,2])) # --> 9 (5 + 4)

# Time Complexitiy = O(n^2)
# Space Complexity = O(1)
# Pattern = Pair comparison + max tracking