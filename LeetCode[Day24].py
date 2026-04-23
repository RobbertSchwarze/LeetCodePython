# Day 24

# Return hoeveel peaks er in de lijst zitten.

# Een peak is een element dat:
# - groter is dan het vorige
# - én groter is dan het volgende

#Expected outputs:

#[1,3,2,4,3,5,1] → 3
#[1,2,3] → 0
#[3,2,1,2,3,2] → 1

def countPeaks(nums: list[int]) -> int:

    peak = 0

    for i in range(0, len(nums) - 2):
        if ( (nums[i + 1]) > (nums[i]) and nums[i + 1] > nums[i + 2]):
            peak += 1
        
    return peak

print(countPeaks([1,2,3,2,4,3,5,1]))
print(countPeaks([1,2,3]))
print(countPeaks([3,2,1,2,3,2]))

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Counting Pattern, Neighbour tracking