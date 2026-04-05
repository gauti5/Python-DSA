# Two Sum 

# Leetcode - Q1 (Two Sum)

# Optimal Solution

def two_sum(arr, target):
    num_index={}
    for i, num in enumerate(arr):
        complement=target-num
        
        if complement in num_index:
            return [num_index[complement], i]
        num_index[num]=i
    return []
    

arr=[2,7,11,15]
target=18
print(two_sum(arr, target))