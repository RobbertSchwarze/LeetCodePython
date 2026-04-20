# Day 15 

# Opdracht:
# Return True als een waarde minstens twee keer voorkomt in de lijst.
# Anders False

# [1, 2, 3, 4 ] --> False
# [1, 2, 4, 1 ] --> True

def hasDuplicate (nums: list[int]) -> bool:

    # Wat we willen doen, is onze eerste in de array vergelijken met de rest van array.
    # Als die dus gevonden wordt returnen we meteen True.
    # Ik neem aan dat we hier een nested for loop for gebruiken.

    # Laten we eerst proberen om gewoon normaal door de for loop heen te komen.

    dplc = False;
      
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] == nums[j] and i != j):
                dplc = True

    return dplc


print(hasDuplicate([1,2,3,4])) # False
print(hasDuplicate([1,2,4,6,4])) # True

        