# Opdracht: 

# Return de kleinste som van een paar (i, j ) waarbij:
# i < j

# Voorbeeld:
# [1,2,3] -> 3 (1 + 2)
# [5,1,4,2] -? 3 (1 + 2)

def minPairSum(nums: list[int]) -> int:

    sum = 0
    minPair = float("inf")

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (i < j ):
                sum = nums[i] + nums[j]
                # Als de sum lager is dan het minPair. maken we minPair gelijk aan de waarde sum. 
                if (nums[i] + nums[j] < minPair):
                    minPair = sum
    
    return minPair

print(minPairSum([1,2,3])) # -> 3
print(minPairSum([5,1,4,2])) # -> 3

                


