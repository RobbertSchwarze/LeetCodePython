# Day 12

# Retourneer de eerste index waar target voorkomt in nums.
# Als target niet voorkomt, return -1.

def firstIndexOf(nums: list[int], target: int) -> int:

    index = 0


    for num in nums:
        # Als de waarde van num gelijk is aan het nummer dat we zoeken, retourneren we meteen de index.
        if num == target:
            return index
        # Als het niet dezelfde waarde is tellen we de positie op.
        index += 1

    
    # Als we uit de loop zijn, en het target is niet gevonden
    return -1

print(firstIndexOf([4,2,9,2,5], 2)) # Output 1
print(firstIndexOf([1,3,5], 2)) # Output -1

# Space Complexity = O(1)
# Time Complexity = O(n)

# Pattern: Search Pattern.
