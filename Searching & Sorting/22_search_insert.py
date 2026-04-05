
# Search Insert Position

def insert(arr, target):
    left=0
    right=len(arr)-1
    
    while left<right:
        mid=(left+right)//2
        
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left
    
    
arr=[1,3,5,6]
target=5
print(insert(arr, target))

"""
# brute force
def insert(arr, target):
    for i in range(len(arr)):
        if arr[i]>=target:
            return i
    return len(arr)

arr=[1,3,5,6]
target=5
print(insert(arr, target))
"""