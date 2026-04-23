# Day 25
#Opdracht:

#Return True als de lijst een “mountain” is.
#Een mountain betekent:
# -eerst strikt stijgend
# -daarna strikt dalend
# -beide delen moeten bestaan (dus niet alleen stijgen of alleen dalen)

#Voorbeelden:
#[1,2,3,2,1] → True
#[1,2,3] → False
#[3,2,1] → False
#[1,2,2,1] → False

def isMountain(nums: list[int]) -> bool:
    # Denk aan een fase change
    # Hij moet eerst up gaan, en dan down.

    # Hij moet eerst stijgend zijn, dan dalend
    
    # Hij heeft geen, gelijke buren, alleen omhoog, of alleen omlaag

    up = False
    down = False

    for i in range(0, len(nums) - 1):
        if (nums[i] == nums[i + 1]):
            return False
        if(nums[i + 1] > nums[i]):
            #print("first if")
            #print("Going up")
            up = True
        if (nums[i] > nums[i + 1]):
            if (up and nums[i] > nums[i + 1]):
                #print("Going down")
                down = True
        if(down and nums[i + 1] > nums[i]):
            #print("Going up")
            return False

    if (up and down):
        return True
    else:
        return False

print(isMountain([1,2,3,2,1]))   # True
print(isMountain([1,2,3,4,2,1])) # True
print(isMountain([1,2,3]))       # False
print(isMountain([3,2,1]))       # False
print(isMountain([1,2,2,1]))     # False
print(isMountain([1,3,5,4,2]))   # True
print(isMountain([1,2,3,2,3]))   # False
print(isMountain([1,2,1]))       # True

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern: State change / phase tracking, boolean checking