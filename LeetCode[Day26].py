# Day 26

#Opdracht:

#Return hoeveel valleys er in de lijst zitten.

#Een valley is een element dat:

#kleiner is dan het vorige
#én kleiner is dan het volgende

#Expected outputs:

#[3,1,4,2,5,1,6] → 3
#[1,2,3] → 0
#[5,3,4,2,3] → 2

def countValleys(nums: list[int]) -> int:

    counting_valleys = 0
    
    for i in range(0, len(nums) - 2):

        if (nums[i + 1] < nums[i] and nums[i + 1] < nums [i + 2]):
            #print("counting valley")
            counting_valleys += 1

    return counting_valleys

print(countValleys([3,1,4,2,5,1,6]))  # 3
print(countValleys([1,2,3]))          # 0
print(countValleys([5,3,4,2,3]))      # 2

print(countValleys([1]))              # 0
print(countValleys([1,2]))            # 0
print(countValleys([2,1,2]))          # 1
print(countValleys([2,1,2,1,2]))      # 2
print(countValleys([3,2,1]))          # 0
print(countValleys([1,2,1]))          # 0
print(countValleys([2,2,2]))          # 0
print(countValleys([3,1,1,3]))        # 0

# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor comparison, counting