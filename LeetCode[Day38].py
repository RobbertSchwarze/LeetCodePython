# Day 38
# Difficulty: 5 / 10

# Task:
# Return how many times the list changes direction.

# A direction change means:
# - numbers were going up, then start going down
# - or numbers were going down, then start going up
# - equal neighbors do not count as direction changes

# Examples:
# [1, 2, 3, 2, 1] -> 1
# [3, 2, 1, 2, 3] -> 1
# [1, 2, 1, 2, 1] -> 3

# Edge Cases:
# [] -> 0
# [1] -> 0
# [1, 2] -> 0
# [1, 1, 1] -> 0
# [1, 2, 3] -> 0
# [3, 2, 1] -> 0
# [1, 2, 2, 1] -> 1
# [1, 1, 2, 1, 1] -> 1


def count_direction_changes(nums: list[int]) -> int:
    
    if ( len(nums) == 0 or len(nums) == 1) :
        return 0
    
    # So we need to count direction changes which means, we need a variable previous_direction, and current_direction
    # We can give the current_direction = 1 and previous_direction = -1 for instance.
    # 1 = going up
    # -1 = going down
    # 0 = equal / no direction

    previous_direction = 0
    count = 0

    for i in range(0, len(nums) - 1):
        # We need to think of when to detect a change.
        # So when we go from up to down, it counts as a change.
        # And when we go from down to up, it counts as a change.

        if (nums[i] < nums[i + 1]):
            current_direction = 1
        elif (nums[i] > nums[i + 1]):
            current_direction = -1
        else:
            current_direction = 0
    
        if (current_direction == 0):
            continue
        
        # No we need a detection, so if the current direction is different from the previous direction.
        # We'll count !
        if (previous_direction != 0 and current_direction != previous_direction):
            count += 1
        
        previous_direction = current_direction 


    return count
        
print(count_direction_changes([1, 2, 3, 2, 1]))     # 1
print(count_direction_changes([3, 2, 1, 2, 3]))     # 1
print(count_direction_changes([1, 2, 1, 2, 1]))     # 3

print(count_direction_changes([]))                  # 0
print(count_direction_changes([1]))                 # 0
print(count_direction_changes([1, 2]))              # 0
print(count_direction_changes([1, 1, 1]))           # 0
print(count_direction_changes([1, 2, 3]))           # 0
print(count_direction_changes([3, 2, 1]))           # 0
print(count_direction_changes([1, 2, 2, 1]))        # 1
print(count_direction_changes([1, 1, 2, 1, 1]))     # 1


# Time Complexity = O(n)
# Space Complexity = O(1)
# Pattern = Neighbor Tracking, Counting 