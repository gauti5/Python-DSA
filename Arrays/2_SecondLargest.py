
"""
def brute_force(arr):
    sorted_arr=sorted(arr, reverse=True) # O(nlogn)
    return sorted_arr[1]


a=[2,3,44,1,333,11,223]
print(f"Second Largest Number : {brute_force(a)}")

"""

def optimal(arr):
    # float("-inf") -> small +ve value (>0 condition)
    largest=secondlargest=float("-inf")
    
    for num in arr:
        if num>largest: 
            secondlargest=largest
            largest=num
        elif num>secondlargest and num!=largest: 
            secondlargest=num
    if secondlargest!=float("-inf"):  
        return secondlargest
    return "Not Found!"

# O(n)
a=[2,3,44,1,333,11,223, 332]
print(f"Second Largest Number : {optimal(a)}")