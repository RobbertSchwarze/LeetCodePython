# Opdracht

# Return de laatste index waar target voorkomt in nums.
# Als target niet voorkomt -> return -1.

def lastIndexOf(nums: list[int], target: int) -> int:

    # We want to keep track of the position in our loop
    index = 0
    # But we need to only assign in to the last_index if it's found on that position
    last_index = -1

    for num in nums:
        if num == target:
            last_index = index
        
        index += 1
    
    # If last_index hasn't been assigned, we still have the -1 as last_index, so we need to return -1.
    if last_index == -1:
        return -1
    else:
        return last_index



print(lastIndexOf([4,2,9,2,5], 2)) # 3
print(lastIndexOf([1, 3, 5], 2)) # -1

# Time Complexity = O(n) 
# Space Complexity = O(1)
# Pattern = Linear Search, Counting Pattern.