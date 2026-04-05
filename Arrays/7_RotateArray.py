# Rotate an array by K position
def rotate(arr,k):
    n=len(arr)
    rotations=k%n
    # Optimal Solution O(n)
    return arr[-rotations:]+arr[:-rotations]
    
    
    # Brute Force
    for _ in range(rotations):
        last_element=arr.pop()
        arr.insert(0, last_element)
    return arr

arr=[1,2,3,4,5]
k=2
print(rotate(arr, k))