# Find the Missing Number in an Array (leetcode - 268)

def missing(arr):
    n=len(arr)
    # Optimal Approach
    exp_sum=n*(n+1)//2
    act_sum=sum(arr)
    return exp_sum-act_sum
    
    
    # Brute Force Approach -> 0(n)
    for i in range(n):
        if i not in arr:
            return i

arr=[0,3,2,5,1]
print(missing(arr))