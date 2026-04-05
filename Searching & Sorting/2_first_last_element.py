# Find the first and last position in sorted array

# leetcode -> 34

# Searching and Sorting (optimal solution)

def first_last(arr, target):
    def find_index(isFirst):
        left=0
        right=len(arr)-1
        index=-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]<target:
                left=mid+1
            elif arr[mid]>target:
                right=mid-1
            else:
                index=mid
                if isFirst:
                    right=mid-1
                else:
                    left=mid+1
        return index
        
    first=find_index(True)
    last=find_index(False)
    return [first, last]

arr=[8,5,7,7,8,8,10]
target=8
print(first_last(arr, target))