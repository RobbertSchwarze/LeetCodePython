# Herhaling [Day4] CountEven
# Counting Pattern

#def countEven(nums: list[int]) -> int:
    #Variabele waar we mee optellen zodat we het terugkrijgen.
    #som = 0

    #for num in nums:
        #if num % 2 == 0:
            #som += 1
    
    #return som

#print(countEven([1, 2, 2, 2, 2]))

# Time Complexity = O(n), want we gebruiken één for-loop
# Space Complexity = O(1), want we gebruiken een constant.

# Day 5, Sum of Positive Numbers

# Probleem: nums = [-2, 3, -1, 5 ,4] 
# Output: 12

def sumPositive(nums: list[int]) -> int:
    # We maken een variabele aan om ervoor te zorgen dat we de positieve getallen kunnen optellen.
    som = 0
    # We lopen door de gegeven lijst heen
    for num in nums:
        #Als de integer hoger is dan 0, tellen we die op bij som.
        if num > 0:
            som += num

    return som

print(sumPositive([-2,3,-1,5,4]))

# Time Complexity = O(n)
# Space Complexity = O(1)
# Welk pattern? Accumulation Pattern

