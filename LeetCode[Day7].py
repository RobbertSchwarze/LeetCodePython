# Day 7
# Edge Case Discipline + Defensive Thinking
# Fundamentele basis.

# Probleem : Find Second Largest
# Gegeven een lijst met integers.
# Return het tweede grootste getal.

# nums = [4,2,9,1,5]
# output = 5

# Wat als lijst maar 1 element heeft? Dan returnen we gewoon de [0] van de lijst.
# Wat als alle getallen hetzelfde zijn?
# Wat als er negatieve getallen zijn?
# Wat als grootste getal meerdere keren voorkomt?

# We trainen, tracken van 2 variabelen.
# Conditionele logica.
# Edge case thinking.
# Correct initialiseren
# Geen extra lijst maken O(1) space complexitiy.

def secondLargest(nums : list[int]) -> int:

    second = nums[0]
    largest = nums[0]

    if len(nums) == 1:
        return nums[0]
    
    if len(nums) != 1:
    # We zoeken eerst de largest
        for num in nums:
            if num > largest:
                largest = num
    
    print("Largest:", largest)
    if len(nums) != 1:        
        for num in nums:
            if num != largest and num > second:
                second = num
    
    return second

print("Second largest number:", secondLargest([-1, 4, 2, 17, 3, 17, 6, 7, 10, 8, 15, 17]))
print("Just one integer in the list: ", secondLargest([1]))

# Time Complexity = O(n)
# Space Complexity = O(1)
# Edge cases; Als de lijst één integer heeft, geeft die gewoon de eerste terug.
# Als alle getallen hetzelfde zijn dan geeft die dat ook terug.
# Als het grootste getal meerdere keren voorkomt, maakt dat niet uit, want we tracken het grootste getal. en zeggen als het second_largest_number niet gelijk is aan de largest integer.
# Als er negatieve getallen zijn slaat die dat gewoon over met de logica die ik geschreven heb.