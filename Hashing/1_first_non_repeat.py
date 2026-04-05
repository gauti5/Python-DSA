
# Find the first non repeating element in an array.

# Brute Force - O(n^2)

def first_non_repeat(arr):
    n=len(arr)
    for i in range(n):
        unique=True
        for j in range(n):
            if i!=j and arr[i]==arr[j]:
                unique=False
                break
        if unique:
            return arr[i]
    return -1

arr=[1,2,1,4,5,3,2]
print(first_non_repeat(arr))
 