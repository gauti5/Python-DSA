# find square root for given number

# leetcode - 69

def square_root(x):
    if x==0 and x==1:
        return 1
    
    left=1
    right=x
    ans=0
    while(left<=right):
        mid=(left+right)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            ans=mid
            left=mid+1
        else:
            right=mid-1
    return ans

x=16
print(square_root(x))