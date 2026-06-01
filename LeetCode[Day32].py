# Day 33
# Moeilijkheid: 5 / 10

# Opdracht:
# Return de lengte van de langste groep van gelijke getallen.
#
# Een groep betekent:
# - één of meerdere dezelfde getallen naast elkaar

# Voorbeelden:
# [1,1,2,2,2,3] -> 3
# [5,5,5,5] -> 4
# [1,2,3] -> 1

# Edge cases:
# [] -> 0
# [1] -> 1
# [1,1,1,2,2,3,3] -> 3
# [1,2,2,3,3,3,2] -> 3
# [4,4,4,4,4] -> 5
# [1,2,2,2] -> 3
# [1,1,2,2,2,3,3,3,3] -> 4


def longestGroup(nums: list[int]) -> int:

    longest_group = float("-inf")
    current_group = 1

    # When length = 0
    if (len(nums) == 0):
        return 0

    if (len(nums) == 1):
        return 1

    # When length = 1

    for i in range(0, len(nums) - 1 ):
        
        # We want a detection when there is a new group
        # We also want a counter to count the currrent_group length
        if ( (nums[i] == nums[i + 1]) ):
            #print(f"Counting current group")
            current_group += 1
        else: 
            #print(f"New group detected !")
            if (current_group > longest_group):
                longest_group = current_group
            
            current_group = 1

        if (current_group > longest_group):
            longest_group = current_group

    
    return longest_group
    

print(longestGroup([1,1,2,2,2,3]))         # 3
print(longestGroup([5,5,5,5]))             # 4
print(longestGroup([1,2,3]))               # 1

print(longestGroup([]))                    # 0
print(longestGroup([1]))                   # 1
print(longestGroup([1,1,1,2,2,3,3]))       # 3
print(longestGroup([1,2,2,3,3,3,2]))       # 3
print(longestGroup([4,4,4,4,4]))           # 5
print(longestGroup([1,2,2,2]))             # 3
print(longestGroup([1,1,2,2,2,3,3,3,3]))   # 4


# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Group Tracking, Neighbor Comparison, Max Tracking