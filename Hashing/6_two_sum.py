# Two Sum 

# Leetcode - Q1 (Two Sum)

# Brute Force - O(n^2)

def two_sum(arr, target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j]==target:
                return [i,j]
    return []

arr=[2,7,11,15]
target=18
print(two_sum(arr, target))