#Day 28

#Return hoeveel keer de lijst verandert van richting:

#stijgend → dalend
#of dalend → stijgend

#Opdracht
def countTransitions(nums: list[int]) -> int:

    transitions = 0
    up = False
    down = False

    for i in range(0, len(nums) - 1):

        if(nums [i] < nums[i + 1]):
            up = True

        if (up and nums[i] > nums[i + 1]):
            up = False
            #print("Going down")
            transitions += 1
        
        if (nums[i] > nums[i + 1]):
            down = True
        
        if (down and nums[i] < nums[i + 1]):
            down = False
            #print("Going up")
            transitions += 1


    return transitions


print(countTransitions([1,2,3,2,1]))      # 1
print(countTransitions([1,2,1,2,1]))      # 3
print(countTransitions([5,4,3,2,1]))      # 0
print(countTransitions([1,2,3,4,5]))      # 0
print(countTransitions([1]))              # 0
print(countTransitions([1,2]))            # 0
print(countTransitions([2,2,2]))          # 0
print(countTransitions([1,2,2,1]))        # 1

# Time Complexity = O(n)
# Space Complexity = O(1)

# Pattern: Direction Tracking, Counting

# Feedback, ik heb hier twee variabelen gebruikt up and down, waarnaar ik misschien beter 'direction' kon bijhouden met variabelen zoals 0, 1, -1.
# Was hier alleen nog niet eerder mee bekend, ik zal experimenteren met die manier van tracking