# Find the Majority Elements in an array
def majority(arr):
    
    # Optimal Approach
    count=0
    x=None
    for num in arr:
        if count==0:
            x=num
        if num==x:
            count+=1
        else:
            count-=1
            
    return x
    
    
    # Brute Force Approach
    for x in set(arr):
        if arr.count(x) > len(arr)//2:
            return x

arr=[1,2,2,2,2,2,4,5,6]
print(majority(arr))