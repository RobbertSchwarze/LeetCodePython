# Day 23

#Opdracht:

#Return de lengte van de langste aaneengesloten stijgende reeks.

#Voorbeeld:

#[1,2,3,2,3,4,5] → 4
#(2,3,4,5)
#[5,4,3] → 1
#[1,2,1,2,3] → 3

def longestIncreasingStreak(nums: list[int]) -> int:
    
    current_streak = 1
    max_streak = 1
    
    for i in range(len(nums) - 1):
        # We willen dus de langste aaneengesloten stijgende reeks tracken.
        if (nums[i + 1] > nums[i]):
            current_streak += 1
            print(f"Current Streak: {current_streak}")
            # Per iteratie zorgen dat de max_streak opgeteld wordt.
            if ( (max_streak) < (current_streak) ):
                max_streak = current_streak
                # Wanneer het volgende nummer lager is. Begint de streak opnieuw.
        elif (nums[i + 1] <= nums[i]):
            current_streak = 1
    
    return max_streak


print(longestIncreasingStreak([1,2,3,2,3,4,5])) # 4
print(longestIncreasingStreak([5,4,3])) # 1
print(longestIncreasingStreak([1,2,1,2,3])) # 3