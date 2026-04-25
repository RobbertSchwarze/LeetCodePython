# Day 27

# Opdracht:
# Return de lengte van de langste aaneengesloten reeks van gelijke getallen.

def longestPlateau(nums: list[int]) -> int:

    current_plateau = 1
    max_plateau = 1

    if ( (len(nums) == 0) ):
        return 0

    for i in range(0, len(nums) -1 ):

        #print(f"Compare: {nums[i]} == {nums[i + 1]}")
        if ( (nums[i]) == (nums[i + 1]) ):
            current_plateau += 1
            # Per iteratie houden we onze max_plateau bij.
            if ( (max_plateau) < (current_plateau) ):
                max_plateau = current_plateau
                #print(f"Max_Plateau: {max_plateau}")
        
        # Hier detecteren we of het plateau is gestopt.
        if( (nums[i]) != (nums[i + 1]) ):
            current_plateau = 1
  
    return max_plateau

print(longestPlateau([1,1,2,2,2,3]))   # 3
print(longestPlateau([5,5,5,5]))       # 4
print(longestPlateau([1,2,3]))         # 1
print(longestPlateau([1]))             # 1
print(longestPlateau([2,2,1,1,1,2]))   # 3


print(longestPlateau([]))              # 0
print(longestPlateau([7,7]))           # 2
print(longestPlateau([1,2,2,3,3]))     # 2

# Time Complexity = O(n)
# Space Complexity = O(1)

# Pattern: Streak Tracking, Neighbor Tracking, Max Tracking
