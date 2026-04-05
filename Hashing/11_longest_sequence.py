# Find the longest consecutive sequence 

# leetcode - Q28

def long_seq(arr):
    
    if not arr:
        return 0
    arr.sort()
    curr=1
    longest=1
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            if arr[i]==arr[i-1]+1:
                curr+=1
            else:
                longest=max(curr, longest)
                curr=1
    return max(curr, longest)

arr=[100,2,200,1,3,5,4]
print(long_seq(arr))