# Find the first non repeating element in an array.

# Optimal Solution - O(n)

def first_non_repeat(arr):
    freq={}
    for i in arr:
        freq[i]=freq.get(i, 0)+1
        print(freq)
    for i in arr:
        if freq[i]==1:
            return i
    return -1

arr=[1,2,1,4,5,3,2]
print(first_non_repeat(arr))