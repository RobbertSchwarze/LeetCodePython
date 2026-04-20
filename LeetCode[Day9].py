# Day 9
# find Min and Max

#def findMinMax(nums: list[int]) -> tuple[int, int]:

    # We declareren eerst de variabelen.
    #max_value = nums[0]
    #min_value = nums[0]

    # We lopen door de lijst heen om het maximum & minimum te vinden
    #for num in nums:
        #if num > max_value:
            #max_value = num
        #elif num < min_value:
            #min_value = num


    #return max_value, min_value

#print(findMinMax([1,3,2,1]))

# Day 9
# Count Strictly Increasing Steps

#Problem:
# nums = [1, 3, 2, 4, 5]
# Output : 3

#def countIncreases(nums: list[int]) -> int:

    #count = 0

    #for i in range(1, len(nums)):
        # Elke keer als het huidige cijfer nums[0] kleiner is dan het cijfer nums [i] + 1 dan willen we er eentje optellen bij count.
        #if nums[i] > nums[i -1]: 
            #count += 1
    
    #return count

#print(countIncreases([1, 3, 2, 4, 5, 4, 6, 7]))

# Space Complexity = O(1)
# Time Complexity = O(n)
# Pattern = Counting Pattern.

def countIncreases(nums: list[int]) -> int:
    
    count = 0

    for i in range(1, len(nums)):
        # Als het huidige cijfer groter is dan het cijfer hiervoor, dan hebben we een stap gemaakt.
        # Dus dan doen we +1.

        # Dit doen we omdat we dan niet met i + 1 de lijst overheen lopen. 
        # We kunnen dit namelijk dus ook doen omdat we, met de 2e in de lijst beginnen, dus - 1 zorgt er ook voor dat we niet uit de lijst komen :)

        if nums[i] > nums[i - 1]:
            count +=1
    
    return count


print(countIncreases([1, 3, 2, 4, 5, 4, 6, 7])) # Output = 5.


   



