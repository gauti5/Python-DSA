
# Bubble Sort -> bubble sort is simplest sorting algorithm that works by repeatly swapping adjancent elements

"""arr=[12,23,34,5,4]
itr-1 :
find largest number and swap with adjancent 
[12, 23, 5, 34, 4]
[12, 23, 5, 4, 34]

itr - 2:
[12, 5, 23, 4, 34]
[12, 5, 4, 23, 34]

itr - 3:
[5, 12, 4, 23, 34]
[5, 4, 12, 23, 34]

itr - 4:
[4, 5, 12, 23, 34] -> output
"""

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
    return arr

arr=[12,23,34,5,4]
print(bubble_sort(arr))