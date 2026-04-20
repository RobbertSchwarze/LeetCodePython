# Opdracht:

# Return de eerste waarde die een duplicate heeft
# (= eerste waarde die je tweede keer ziet)

# Als er geen duplicate return -1

# Voorbeeld:
# [1,2,3,1,2] -> 1
# [2,1,3,5,3,2] -> 3
# [1,2,3,4] -> -1

# Set is nieuw voor mij, dus dit is een learning concept.
# Ik heb vooral met for-loops gewerkt. Nog nooit van Set gehoord.

def firstDuplicate (nums: list[int]) -> int:

    # Seen wordt onze nieuwe lijst
    # In seen kunnen geen duplicates komen.
    seen = set()

    for num in nums:
        # Met deze regel kan je er dus voor zorgen dat, als het nummer al in de lijst staat.
        # Wat automatisch dan ook de eerste is die je tegenkomt.
        # Retourneren we dat nummer.
        if num in seen:
            return num
        # We voegen ons eerste cijfer toe aan de lijst seen
        seen.add(num)

    return -1
           
print(firstDuplicate([1,2,3,1,2]))
print(firstDuplicate([2,1,3,5,3,2]))
print(firstDuplicate([1,2,3,4]))

# Time Complexity = O(n)
# Space Complexity = O(n)