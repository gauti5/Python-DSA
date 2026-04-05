# Find Single Number from an array

# Leetcode - Q136

# Optimal Solution

def single_number(nums):
    freq={}
    for num in nums:
        freq[num]=freq.get(num, 0)+1
    for num in nums:
        if freq[num]==1:
            return num

nums = [4,1,2,1,2]
print(single_number(nums))