# Day 21

# Opdracht:
# Return hoeveel 'unieke waarden' in de lijst zitten

# Voorbeeld 
# [1,2,2,3,3,3] -> 3
# [5,5,5,5] -> 1
# [1,2,3,4] -> 4

def countUnique(nums: list[int]) -> int:

    seen = set()

    for num in nums:
        # Nu voegen we het nummer toe aan de lijst set
        seen.add(num)
     
     # Daarna retourneren we de lengte van de lijst, sinds er dus geen dubbele integers kunnen komen hebben we altijd unieke cijfers.
    return len(seen)


print(countUnique([1,2,2,3,3,3]))
print(countUnique([5,5,5,5]))
print(countUnique([1,2,3,4]))

# Time Complexity = O(n) -> het algoritme heeft n stappen. 
# Space Complexity = O(n) -> set groeit met input 

# Pattern = HashSet / Unique Tracking
