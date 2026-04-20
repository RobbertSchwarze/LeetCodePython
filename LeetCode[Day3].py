# Day 1 - Find the Maximum!

# Problem
# Given a list of integers,
# return the largest number in the list.

# Example
# nums = [3, 7, 2, 9, 5]
# Output: 9

# What we're training today,
# Looping through a list
# Basic algorithm thinking.

# Think before coding
# How do you remember the biggest number so far? nums[i] > nums[i] + 1
# What should the starting value be ? first of the list no?
# What do you do for each number in the list? we loop through it, compare it with the next number and see if it's bigger, if it's bigger we tie it to a variable.

# Level 1
#def findMax(nums: list[int]) -> int:

    #max_number = nums[0] # O(1)

    #for num in nums:
        #if num > max_number:
            #max_number = num

    #return max_number
        
#print(findMax([3,2,7,9,5]))

# Time Complexity = How fast it grows
# It measures how the number of operations grow when input gets bigger.
# O(1) -- Constant time
# Same speed no matter how big the input is.
# Example: x = nums[0]
# Always 1 operation.

# O(n) -- Linear Time.
# You go through this list once ! for num in nums:
# If list has 5 elements -> 5 steps
# If list has 1,000 elements -> 1000 steps.
# Grows linearly.

#O(n^2) Quadratic time
# Nested loops.
# for i in nums:
# for j in nums:
# if n = 100 -> 100 x 100 = 10,000
# gets slow fast.

# Okay so this is Level 2.
# We are trying to not compare the element with itself.
# This is more sufficient since you do less checking ofcourse.y

#def findMax(nums: list[int]) -> int:

    #max = nums[0]

    #for num in nums[1:]:
        #if num > max:
            #max = num

    #return max

#print(findMax([3,7,2,9,5]))

# We now do level 3. it's the most efficient way.
# This is still O(n), but cleaner and idiomatic.
# Only if they allow build ins.
# If they say "Don't use built-ins functions we use the manual loop ofcourse."

def findMax(nums: list[int]) -> int:
    return max(nums)

print(findMax([3,7,2,9,5]))