
# Leet code (Move Zeros)

def move_zeros(arr):
    n=len(arr)
    
    # Optimal Solution
    pointer=0
    
    for i in range(n):
        if arr[i]!=0:
            arr[pointer], arr[i]=arr[i], arr[pointer]
            pointer+=1
    return arr
    
    # O(n) -> Brute Force
    non_zeros=[num for num in arr if num!=0]
    zeros=n-len(non_zeros)
    result=non_zeros+[0]*zeros
    
    for i in range(n):
        arr[i]=result[i]
    return arr

arr=[0,2,1,0,4,5,0]
print(move_zeros(arr))