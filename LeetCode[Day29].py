#Day 30
#Moeilijkheid: 5 / 10

#Opdracht:

#Return hoeveel “direction runs” er zijn.

#Een run is een aaneengesloten stuk dat:
#stijgt
#of daalt
#Gelijke waarden tellen niet als richting.


def countDirectionRuns(nums: list[int]) -> int:

    count_direction_run = 0

    # We maken 3 verschillende waarden van states.
    # current_direction_up = 1
    # current_direction_down = -1
    # current_direction_none = 0

    current_direction = 0
    previous_direction = 0

    for i in range (0, len(nums) - 1):

    # Up
        if (nums[i] < nums[i + 1]):
            current_direction = 1
    
    # Down 
        if (nums[i] > nums[i + 1]):
            current_direction = -1
    
    #None
        if (nums[i] == nums[i + 1]):
            current_direction = 0
    
        if (current_direction == 0):
            continue
    
        # Detecting different direction !
        if (current_direction != previous_direction):
            count_direction_run += 1

        # 
        previous_direction = current_direction

    return count_direction_run


print(countDirectionRuns([1,2,3,2,1]))      # 2
print(countDirectionRuns([1,2,1,2,1]))      # 4
print(countDirectionRuns([5,4,3,2]))        # 1
print(countDirectionRuns([1,1,1]))          # 0
print(countDirectionRuns([1,2,2,3,2]))      # 2

# Time Complexity = O(n)
# Space Complexity = O(1)

# Pattern: Direction Tracking, State Tracking, Counting, Neighbor Comparison