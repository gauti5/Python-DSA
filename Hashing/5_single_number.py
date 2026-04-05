# Find Single Number from an array

# Leetcode - Q136

# Bit Manipulation 

def single_number(nums):
    result=0
    for i in nums:
        result=result^i
    return result


nums = [4,1,2,1,2]
print(single_number(nums))