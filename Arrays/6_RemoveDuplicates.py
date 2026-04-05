# Remove Dupicates from sorted array

# Leetcode Question No : 26

def sorted_array(arr):
    k=1
    for n in range(1, len(arr)):
        if arr[n]!=arr[n-1]:
            arr[k]=arr[n]
            k+=1
    return arr

arr=[1,2,2,3,4,4,4,5,6,6,6,6,7]
print(f"Duplicates : {sorted_array(arr)}")
    