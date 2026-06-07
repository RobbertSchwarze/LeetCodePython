# Day 35
# Difficulty: 4.5 / 10

# Task:
# Return how many times the value changes compared to the previous number.

# Examples:
# [1,1,2,2,3] -> 2
# [5,5,5] -> 0
# [1,2,3] -> 2

# Edge Cases:
# [] -> 0
# [1] -> 0
# [1,1] -> 0
# [1,2] -> 1
# [1,2,2,3,3,1] -> 3


def countValueChanges(nums: list[int]) -> int:

    # Okay so we have to start detecting how many times the value changes,
    # Small detection on hey, a number is different, let's count !

    change_detected= 0

    for i in range(0, len(nums) - 1):

        # So if the following number doesn't equal the previous number, we're detecting a change.
        if ( (nums[i] != nums[i + 1]) ):
            # The detection triggers our counter
            change_detected += 1

    return change_detected 

print(countValueChanges([1,1,2,2,3]))       # 2
print(countValueChanges([5,5,5]))           # 0
print(countValueChanges([1,2,3]))           # 2

print(countValueChanges([]))                # 0
print(countValueChanges([1]))               # 0
print(countValueChanges([1,1]))             # 0
print(countValueChanges([1,2]))             # 1
print(countValueChanges([1,2,2,3,3,1]))     # 3


# Time Complexity =
# Space Complexity =
# Pattern =