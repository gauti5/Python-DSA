# Maximum Subarray (leetcode - Q53)

def max_subarray(arr):
    
    # Optimal solution -> Kadane's algorithm
    
    max_sum=arr[0]
    curr_sum=arr[0]
    
    for i in range(1, len(arr)):
        curr_sum=max(arr[i], curr_sum+arr[i])
        max_sum=max(max_sum, curr_sum)
    return max_sum
    
    # Brute Force
    max_sum=float("-inf")
    for i in range(len(arr)):
        cur_sum=0
        for j in range(i, len(arr)):
            cur_sum+=arr[j]
            max_sum=max(max_sum, cur_sum)
    return max_sum


arr=[1,2,4,5,-6,43,1,32,12,11,1]
print(max_subarray(arr))