# Leetcode -> 278

def bad_version(n, bad):
    low=1
    high=n

    while low<high:
        mid=(low+high)//2

        if isBadVersion(mid):
            high=mid
        else:
            low=mid+1
    return low

n=5,
bad=4
print(bad_version(n, bad))