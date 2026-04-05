# Contain Duplicate - Sorting

# Leetcode -> Q217
def contain_duplicate(nums, k):
    dup={}
    for i, num in enumerate(nums):
        if num in dup:
            if abs(i-dup[num])<=k:
                return True
        dup[num]=i
    return False

nums=[1,22,2,34]
k=2
print(contain_duplicate(nums, k))