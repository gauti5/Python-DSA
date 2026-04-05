## Insertion Sort : comparing with next elements and if its small values then swap
# (n^2)
'''
arr=[1,5,4,2]
itr - 1 : [1,5] compare
[1,5,4,2]
itr - 2: [1,5,4]
[1,4,5]
itr - 3: [1,4,5,2]
[1,2,4,5] -> output
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        pick=arr[i]
        j=i-1
        while j>=0 and arr[j]>pick:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=pick
    return arr
arr=[12,23,34,5,4]
print(insertion_sort(arr))