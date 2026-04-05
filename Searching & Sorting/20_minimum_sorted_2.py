# Find Minimum in rotated sorted array

# Optimal Solution 

# Leetcode -> 153

def sorted(arr):
    left=0
    right=len(arr)-1
    
    while left<right:
        mid=(left+right)//2
        
        if arr[mid]>arr[right]:
            left=mid+1
        else:
            right=mid
    return arr[left]
            
arr=[3,4,5,1,2]
print(sorted(arr))