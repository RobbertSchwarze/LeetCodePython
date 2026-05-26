# Day 31
# Moeilijkheid: 4.5 / 10

# Opdracht:
# Return hoeveel groepen van gelijke getallen er zijn.
#
# Een groep betekent:
# - één of meerdere dezelfde getallen naast elkaar

# Voorbeelden:
# [1,1,2,2,2,3] -> 3
# [5,5,5] -> 1
# [1,2,3] -> 3

# Edge cases:
# [] -> 0
# [1] -> 1
# [1,1,1,2,2,3,3] -> 3
# [1,2,2,3,3,3,2] -> 4


def countGroups(nums: list[int]) -> int:

    # We have to count the unique group

    # Our integer starts with 1, because if we get in the for loop, we always have a starting group.
    groups = 1

    if (len(nums) == 0):
        return 0

    if (len(nums) == 1):
        return 1

    for i in range(0, len(nums) - 1):
        
        # We want to detect a unique integer (this is so we can count a new group)
        if ( nums[i] != nums[i + 1] ):
            groups += 1
    
    return groups

print(countGroups([1,1,2,2,2,3]))     # 3
print(countGroups([5,5,5]))           # 1
print(countGroups([1,2,3]))           # 3
print(countGroups([]))                # 0
print(countGroups([1]))               # 1
print(countGroups([1,1,1,2,2,3,3]))   # 3
print(countGroups([1,2,2,3,3,3,2]))   # 4


# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Counting Pattern, Neighbor Tracking