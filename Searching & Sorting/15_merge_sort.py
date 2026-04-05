# Merge Sort follows divide and conquer, recursively dividing the input into smaller sub arrays and sorting those sub arrays and merging them back..

'''
arr=[38,27,43,10]
[38,27] & [43,10]

[27, 38], [10,43]

[10,27,38,43]
'''
def merge(left, right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left, right)

arr=[38,27,43,10]
print(merge_sort(arr))

