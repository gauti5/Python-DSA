# Quick Sort -> Quick Sort is sorting algorithm based on divide and conquor that picks an element as a pivot and paritions the array around the picked pivot by placing the pivot in its correct position.

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    
    return quick_sort(left)+[pivot]+quick_sort(right)


arr=[38,27,43,10]
print(quick_sort(arr))