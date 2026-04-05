# Intersection of two arrays (leetcode - 349)

def intersection(arr1, arr2):
    m=len(arr1)
    n=len(arr2)
    result=[]
    # Optimal Approach -> O(min(m,n))
    return list(set(arr1) & set(arr2))

    
    
    # Brute Force Approach -> O(m*n)
    if m>n:
        for num in arr1:
            if (num in arr2) and (num not in result):
                result.append(num)
    else:
        for num in arr2:
            if (num in arr1) and (num not in result):
                result.append(num)
    return result

arr1=[1,2,3,4,5]
arr2=[3,4,5,6,7,1]

print(intersection(arr1, arr2))