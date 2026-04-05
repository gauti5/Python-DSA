# Check if an array is sorted ?

def array_sorted(arr):
    # return all(arr[num]<arr[num+1] for num in range(len(arr)-1)) # Optimal Solution
    
    # Brute Force
    n=len(arr)
    for num in range(len(arr)-1):
        if arr[num]>arr[num+1]:
            return False
    return True



arr=[2,3,4]
print(f"Array Sorted : {array_sorted(arr)}")