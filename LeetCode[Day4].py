# Day 1 Review

#def findMax(nums : list[int]) -> int:

# We beginnen het maximum nummer met de eerste in de lijst, zodat we niet het eerste cijfer te hoeven vergelijken van de lijst.
    #max = nums[0]

# Daarna lopen we door de gegeven lijst slaan we dus het eerste cijfer over omdat we die al hebben als max variabele.
    #for num in nums[1:]:
        # Als max kleiner is dan het nummer in de lijst.
        #if max < num:
            # Dan willen we we dat max nu het grotere nummer wordt. 
            #max = num
# Nu retourneren we onze max cijfer, zodat we kunnen uitprinten wat het grootste cijfer in de lijst is.
    #return max

#print(findMax([1, 2, 10, 4, 6 ,7]))

# O(n) tijd
# O(1) ruimte

# Day 2
# Probleem: Count Even Numbers
# Gegeven een lijst met integers
# Return hoeveel getallen even zijn.
# nums = [1,2,3,4,6]
# Output = 3, want 2, 4, 6 zijn even.

# Dit heet het Counting Pattern
# We gebruiken hier de Module Operator %, dit zorgt dat je kan zien wat je overhoudt als je het deelt.

def countEven(nums: list[int]) -> int:
    # We maken een integer zodat we onze getallen kunnen optellen, die noemen we sum
    sum = 0

    # We lopen door de lijst heen
    for num in nums:
        #Bij elk integer willen we weten als we het door 2 delen of we 0 overhouden,
        #Zo kunnen we er namelijk achter komen of het hele integers zijn.
        if num % 2 == 0:
            # Als de integer heel is, zeggen we; 'ik heb er één gevonden' dus ik tel 1 op bij onze variabele.
            sum += 1
    
    return sum

print(countEven([1,2,3,4,6]))

# Onze ruimte is O(1), want we gebruiken sum = 0 ?
# Onze tijdcomplexiteit is O(n) want we lopen door de een lijst heen, dus we maken meerdere stappen.
