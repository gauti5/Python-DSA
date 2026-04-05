"""
Selection Sort -> Comparsion based sorting, it sorts repeatedly selecting the smallest element

arr=[12,23,34,5,4]
itr - 1 : smallest =4, current=12
[4, 23, 34, 5, 12]

itr - 2: current=23, samllest=5
[4, 5, 34, 23, 12]

itr - 3: current = 34, smallest=12
[4,5,12,23,34] -> output
"""
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index]=arr[min_index], arr[i]
    return arr

arr=[12,23,34,5,4]
print(selection_sort(arr))