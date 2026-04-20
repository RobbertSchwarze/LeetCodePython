# Day 11.

# Gegeven een lijst integers.
# Return True als de lijst strictly increasing is.
# Anders False. 

def isStrictlyIncreasing(nums :list[int]) -> bool:

# Als de lijst maar 1 waarde heeft returnen we meteen True. 
    if len(nums) < 2:
        return True
    
    # We lopen door de lijst heen, we beginnen bij nums[1]
    # We willen True terug geven, wanneer de lijst strictly increasing is.
    # Dus als dat niet zo is, returnen we meteen False.
    # Dus als nums[1] (2) kleiner of gelijk is aan nums[0], het cijfer ervoor. Returnen we meteen False.
    # Als dat niet zo is retourneren we True, dus als die wel oploopt :)
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            return False
    
    return True
    
print(isStrictlyIncreasing([1,2,3,4])) # True
print(isStrictlyIncreasing([1,2,2,3])) # False  
print(isStrictlyIncreasing([5]))    # True


# Space Complexity = O(1)
# Time Complexity = O(n)
# Pattern; Boolean checking / early exit.

