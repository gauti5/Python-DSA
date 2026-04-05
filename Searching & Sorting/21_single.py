# Find a single element in an array

def single(arr):
    left=0
    right=len(arr)-1
    
    while left<right:
        mid=left+(right-left)//2
        
        if mid%2==1:
            mid=mid-1
        if arr[mid]==arr[mid+1]:
            left=mid+2
        else:
            right=mid
    return arr[left]

arr = [1,1,2,3,3,4,4,8,8]
print(single(arr))