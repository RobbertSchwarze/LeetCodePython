# Day 22

# Opdracht:

# Return True als er ergens in de lijst een getal groter is dan het vorige getal
# Anders False.

# Expected Outputs:

#[5,4,3,2] → False
#[5,4,6,2] → True
#[1] → False

def hasIncrease(nums: list[int]) -> bool:

    if (len(nums) == 1 ):
        return False
    
    for i in range(len(nums) - 1):
        if (nums[i + 1] > nums[i]):
            return True
        
    return False
              
print(hasIncrease([5,4,3,2])) # False
print(hasIncrease([5,4,6,2])) # True
print(hasIncrease([1])) # False