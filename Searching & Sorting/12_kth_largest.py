def kth_largest(arr, k):
    arr.sort()
    return arr[-k]
    
arr=[2,3,45,1,223,12]
k=2
print(kth_largest(arr, k))

