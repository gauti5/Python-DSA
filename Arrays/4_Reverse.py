# Reverse the Elements of an array

def reverse(arr):
    
    # return arr[::-1] # Optimal Solution
    
    # Brute Force
    n=len(arr)
    for i in range(n//2):
        arr[i], arr[n-1-i]=arr[n-1-i], arr[i]
    return arr
        

arr=[2,3,4,5,6]
print(f"Reversed Array : {reverse(arr)}")