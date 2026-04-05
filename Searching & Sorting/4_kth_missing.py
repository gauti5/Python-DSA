# Kth Missing positive number
# leetcode - Q1539

# Brute Force 

def kth_missing(arr, k):
    missing=[]
    num=1
    i=0
    while len(missing)<k:
        if i<len(arr) and arr[i]==num:
            i+=1
        else:
            missing.append(num)
        num+=1
    return missing[-1]


arr=[2,3,4,7,11]
k=5
# missing values = [1,5,6,8,9,10,12] 5th values is 9

print(kth_missing(arr, k))