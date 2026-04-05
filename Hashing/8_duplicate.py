# Contain Duplicate - Hashing

# Leetcode -> Q217
def contain_duplicate(arr):
    checking=set()
    for n in arr:
        if n in checking:
            return True
        checking.add(n)
    return False

arr=[1,22,2,34]
print(contain_duplicate(arr))

