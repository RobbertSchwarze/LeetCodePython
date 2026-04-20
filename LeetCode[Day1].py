# Day 1 --- SUM1..n

#Task
#Write a function that reutrns the sum of numbers from 1 to n (inclusive).
#Examples, n = 4 --> 10
# n = 1 --> 1
# n = 0 -->

def sum_to_n(n : int) -> int:
    
    sum = 0
    for i in range(1, n + 1):
        sum += i
    
    return sum

print(sum_to_n(4))
print(sum_to_n(1))
print(sum_to_n(0))




