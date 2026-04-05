# Find Minimum in rotated sorted array

# Brute Force

# Leetcode -> 153

def sorted(arr):
    result=arr[0]
    for n in arr:
        if n<result:
            result=n
            
    return result
            

arr=[3,4,5,1,2]
print(sorted(arr))