# Review - Second Largest
# Lijst heeft minstens 2 elementen
# O(n) tijd
# O(1) space
# Werkend voor negatieve getallen
# Werkend voor duplicates.

# Gegeven een integer array nums.
# return het tweede grootste unieke getal in de array.
# Als er geen tweede grootste unieke waarde bestaat return -1.

#def secondLargest(nums: list[int]) -> int:

    # Als de lengte van de lijst kleiner dan 2 is retourneren we 1.
    #if len(nums) < 2:
        #return -1
    
    #largest = nums[0]
    # We zetten het tweede grootste nummer als standaard op de zo laagste mogelijke nummer.
    #second = float("-inf")

    # We zoeken de largest integer
    #for num in nums:
        #if num > largest:
            #largest = num
    
    # We zoeken second largest integer
    #for num in nums:
        #if num != largest and num > second:
            #second = num
    
    #if second == float("-inf"):
        #return -1
    
    #return second

# Example 1
#print(secondLargest([4,2,9,1,5])) # 5
# Example 2
#print(secondLargest([5,4])) # 4
# Example 3
#print(secondLargest([5,5,5])) # -1
# Example 4
#print(secondLargest([2,2,3,3])) # 2
# Example 5
#print(secondLargest([-1,-4,-6,10,5])) # 5
# Example 6
#print(secondLargest([7])) #-1 # Fixed
# Example 7
#print(secondLargest([2,3,2])) #2
# Example 8
#print(secondLargest([10, 8, 9])) #9
# Example 9 
#print(secondLargest([4, 2, 9, 8, 5])) # 8 wordt 5. 

# Deel 1 Mini-versie second largest.
# Probleem - Find Largest en Smallest.

# Gegeven een lijst integers

# Return; het grootste getal
# Return; het kleinste getal.

# Voorbeeld: nums = [4,2,9,1,5]
# output: (9, 1)

#def findMinMax(nums: list[int]) -> tuple [int, int]:

    # We declareren eerst de twee integers die we moeten vinden, maximum en minimum in de lijst.
    #max_value = nums[0]
    #min_value = nums[0]

    #we lopen door de for loop heen om het maximum te vinden
    #for num in nums:
        #if num > max_value:
            #max = num
    
    #print(max)
    
    #we lopen door een for loop om een minimum te vinden
    #for num in nums:
        #if num < min:
            #min = num

    #return max, min

#print(findMinMax([4,2,9,1,5]))

# Het kan ook met één for-loop wordt er gezegd, daar ga ik nu achterkomen hoe dat moet.

def findMinMax(nums: list[int]) -> tuple [int, int]:

    # We declareren eerst de twee integers die we moeten vinden, maximum en minimum in de lijst.
    max_value = nums[0]
    min_value = nums[0]

    #we lopen door de for loop heen om het maximum te vinden
    for num in nums:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num

    return max_value, min_value

print(findMinMax([4,2,9,1,5]))