"""Given an array of integers nums, return the value of the largest element in the array

Example :

Input: nums = [3, 3, 6, 1]

Output: 6

Explanation: The largest element in array is 6

"""

def largest_number(nums):
    largest=nums[0]
    for i in range(len(nums)):
        if nums[i]>largest:
            largest=nums[i]
    return largest

arr_list=[3, 3, 6, 1, 2, 22, 111, 23]
print(largest_number(arr_list))