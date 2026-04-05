# Find the first missing postitive number

# Optimal Solution

# leetcode - 41 (hard)

def first_missing(arr):
    n=len(arr)
    for i in range(n):
        while 1<=arr[i]<=n and arr[arr[i]-1]!=arr[i]:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            
    for i in range(n):
        if arr[i]!=i+1:
            return i+1
    return n+1

arr=[3,4,-1,1]
# arr=[1,2,0] # 3

print(first_missing(arr))