# Brute Force Approach
def largest_number(arr):
    max_num=arr[0]
    for n in arr:
        if n>max_num:
            max_num=n
            
    return max_num


a=[1,2,33,4,11,2221,3342,112,34]
print(f"Largest Number : {largest_number(a)}")

# Optimal Solution
# print(f"Largest Number : {max(a)}")