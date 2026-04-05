# Find the first and last position in sorted array

# leetcode -> 34

# Brute Force

def first_last(arr, target):
    first=-1
    last=-1
    for i in range(len(arr)):
        if arr[i]==target:
            if first==-1:
                first=i
            last=i
    return [first, last]

arr=[8,5,7,7,8,8,10]
target=8
print(first_last(arr, target))