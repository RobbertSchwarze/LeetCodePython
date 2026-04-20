# Day 10 Count Decreases.

# Gegeven een lijst met integers.
# Return hoeveel keer het getal kleiner is dan het vorige getal.

def countDecreases(nums: list[int]) -> int:

    count = 0

    for i in range(1, len(nums)):
        # Als nums[i] kleiner is dan het vorige getal.
        if nums[i] < nums[i - 1]:
            # Dan tellen we er één bij op.
            count += 1


    return count

print(countDecreases([5,3,4,2,1])) # Expected output = 3.

# Space Complexity = O(1)
# Time Complexity = O(n)
# Pattern = Counting Pattern
