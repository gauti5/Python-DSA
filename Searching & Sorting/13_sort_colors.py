# Sort Colors 

# leetcode - 75
def sort_colors(arr):
    zeros, ones, twoes = [], [], []
    for num in arr:
        if num==0:
            zeros.append(num)
        elif num==1:
            ones.append(num)
        else:
            twoes.append(num)
    arr[:]=zeros+ones+twoes
    return arr

arr=[2,0,2,1,1,0]
print(sort_colors(arr))