# Day 32
# Moeilijkheid: 5 / 10

# Opdracht:
# Return de lengte van de kortste groep.
#
# Een groep betekent:
# - één of meerdere dezelfde getallen naast elkaar

# Voorbeelden:
# [1,1,2,2,2,3] -> 1
# [5,5,5] -> 3
# [1,2,3] -> 1

# Edge cases:
# [] -> 0
# [1] -> 1
# [1,1,1,2,2,3,3] -> 2
# [1,2,2,3,3,3,2] -> 1
# [4,4,4,4,4] -> 5


def shortestGroup(nums: list[int]) -> int:

    # Eerst maken we de variabelen aan, ik wil een length_previous_group, lentgh_current_group en shortest_group
    length_current_group = 1
    shortest_group = float("inf")

    # First we detect if the length of the array = 0
    if (len(nums) == 0 ):
        return 0
    
    # Then we detect if the length of the array = 1
    if (len(nums) == 1):
        return 1
    
    # Now, we walk through the array.
    for i in range(0, len(nums) -1 ):

        # It's important to detect when there is a group
        if ( (nums[i] == nums[i + 1]) ):
            #print("Detected group !")
            #
            #  So now it's important to count the length of this particular group
            length_current_group += 1
            #print(f"length_of_current_group = {length_current_group}")
        else:
            if (length_current_group < shortest_group):
                shortest_group = length_current_group
                
            length_current_group = 1
    
    if (shortest_group > length_current_group):
        shortest_group = length_current_group

    return shortest_group
    
print(shortestGroup([1,1,2,2,2,3]))      # 1
print(shortestGroup([5,5,5]))            # 3
print(shortestGroup([1,2,3]))            # 1
print(shortestGroup([]))                 # 0
print(shortestGroup([1]))                # 1
print(shortestGroup([1,1,1,2,2,3,3]))   # 2
print(shortestGroup([1,2,2,3,3,3,2]))   # 1
print(shortestGroup([4,4,4,4,4]))       # 5
print(shortestGroup([1,2,2,2]))         # 1 


# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Counting Pattern, Neighbor Comparison