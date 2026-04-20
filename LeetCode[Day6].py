# Review Day 5
# Pattern: Accumulation

#def sumPositive(nums: list[int]) -> int:
    #total = 0

    #for num in nums:
        #if num > 0:
            #total += num

    #return total

# Time Complexity? O(n)
# Space Complexity? O(1)
# Waarom is dit geen counting pattern? 
# Omdat we niks counten maar we tellen een aantal waardes van de lijst bij elkaar op.

# Day 6
# Find the minimum.
# Gegeven een lijst integers. Return the smallest number.
# Voorbeeld:
# nums = [4,2,9,1,5]
# Output: 1

# Dit lijkt op findMax, maar let op edge cases. 

def findMin(nums: list[int]) -> int:
    
    # We zorgen dat we de eerste variabele assignen naar de eerste waarde van de lijst.
    minimum = nums[0]

    # We lopen door de loop heen van de gegeven lijst, we slaan het eerste cijfer in de lijst over voor optimalisatie.
    for num in nums[1:]:
        # Als de huidige integer is kleiner dan het minimum.
        if num < minimum:
            # Dan is de minimum waarde, nu het kleinere integer.
            minimum = num
    
    return minimum

print(findMin([4,2,9,1,5]))

# Time Complexity = O(n)
# Space Complexity = O(1)
# Welk pattern ? Selection Pattern, Tracking. We tracken de beste waarde tot nu toe.

# Tot nu toe hebben we 3 fundamentele patterns geleerd. 
# 1. Counting Pattern -> += 1
# 2. Accumulation Pattern += num
# 3. Tracking Pattern -> beste waarde bijhouden.
