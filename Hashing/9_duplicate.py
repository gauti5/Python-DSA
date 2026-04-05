# Contain Duplicate - Sorting

# Leetcode -> Q217
def contain_duplicate(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i]==arr[i-1]:
            return True
        
    return False

arr=[1,22,2,2,34]
print(contain_duplicate(arr))