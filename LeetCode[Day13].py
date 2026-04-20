# Opdracht:

# Return hoe vaak target voorkomt in de lijst nums

def countTarget(nums: list[int], target: int) -> int:

    index = 0

    for num in nums:
        if num == target:
            index += 1
    

    return index

# Space Complexity = O(1)
# Time Complexity = O(n)
# Pattern: Search Pattern / Counting Pattern

print(countTarget([1,2,2,3,2], 2)) # 3
print(countTarget([4,5,6], 1)) # 0