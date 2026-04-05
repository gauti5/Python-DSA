# Find Single Number from an array

# Leetcode - Q136 (will get time limit exceeded error)

# Brute Force

def single_number(nums):
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(n):
            if nums[i]==nums[j]:
                count+=1
        if count==1:
            return nums[i]
nums = [4,1,2,1,2]
print(single_number(nums))