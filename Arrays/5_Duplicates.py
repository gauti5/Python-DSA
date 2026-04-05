# Remove Duplicates from an array

def duplicates(arr):
    
    # return list(set(arr)) # Optimal Solution
    
    # Brute Force Approach
    unq=[]
    for n in arr:
        if n not in unq:
            unq.append(n)
    return unq

arr=[1,2,45,55,55,55,66,2,1,34,55]
print(f"Unique Array : {duplicates(arr)}")