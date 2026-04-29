# Find the Majority Elements in an array
def majority(arr):
    
    # Optimal Approach
    count=0
    x=None
    for num in arr:
        if count==0:
            x=num
        if num==x:
            count+=1
        else:
            count-=1
            
    return x
    
    
    # Brute Force Approach
    for x in set(arr):
        if arr.count(x) > len(arr)//2:
            return x

arr=[1,2,2,2,2,2,4,5,6]
print(majority(arr))


'''
def majority_element(arr):
    freq = {}
    n = len(arr)

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

        if freq[num] > n // 2:
            return num

    return None  # if no majority element exists


# Example
arr = [2, 2, 1, 2, 3, 2, 2]
print(majority_element(arr))

'''

'''
def most_repeating(arr):
    freq = {}

    # Count frequency
    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    # Find element with maximum frequency
    max_count = 0
    result = -1

    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            result = key

    return result

'''