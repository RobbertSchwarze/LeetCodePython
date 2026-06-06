# Day 34
# Moeilijkheid: 5.5 / 10

# Opdracht:
# Return hoeveel groepen een lengte van minimaal 2 hebben.
#
# Een groep betekent:
# - één of meerdere dezelfde getallen naast elkaar
#
# We tellen alleen groepen met lengte >= 2

# Voorbeelden:
# [1,1,2,2,2,3] -> 2
# [5,5,5,5] -> 1
# [1,2,3] -> 0

# Edge cases:
# [] -> 0
# [1] -> 0
# [1,1] -> 1
# [1,1,1,2,2,3,3] -> 3
# [1,2,2,3,3,3,2] -> 2
# [4,4,4,4,4] -> 1


def countLargeGroups(nums: list[int]) -> int:

    # We moeten groepen retourneren met een minimale lengte van 2.
    # Een groep betekent één of meerdere dezelfde getallen naast elkaar. okay.

    groups_bigger_than_2 = 0
    current_length = 1

    if (len(nums) == 0 or len(nums) == 1):
        return 0
    
    for i in range(0, len(nums) - 1):

        # First let's throw in an if to detect groups.

        if ( (nums[i] == nums[i + 1]) ):
            #print("comparison detected, this is a group")
            # We also need to count the length of this group ofcourse
            current_length += 1        
        else: 
            #print("new group detected")
            # If we detect a new group, we have to first compare if the current_length >= 2 so we can count a full group.
            if( (current_length >= 2) ):
                groups_bigger_than_2 += 1
                # Then we will reset the current_length to 1, because we're in a new group.
        
            current_length = 1

    # If the loop finished, then we also have to think? Was there a group >= 2?
    if ( (current_length >= 2) ):
            groups_bigger_than_2 += 1

    return groups_bigger_than_2
            
print(countLargeGroups([1,1,2,2,2,3]))      # 2
print(countLargeGroups([5,5,5,5]))          # 1
print(countLargeGroups([1,2,3]))            # 0

print(countLargeGroups([]))                 # 0
print(countLargeGroups([1]))                # 0
print(countLargeGroups([1,1]))              # 1
print(countLargeGroups([1,1,1,2,2,3,3]))   # 3
print(countLargeGroups([1,2,2,3,3,3,2]))   # 2
print(countLargeGroups([4,4,4,4,4]))       # 1


# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Group Tracking, Counting, Neighbor Comparison