# Top K frequent elements

# Leetcode -> 347 

# Hashing

def topk_fre(arr, k):
    freq=[]
    for n in arr:
        freq[n]=freq.get(n, 0)+1
    sorted_arr=sorted(freq.items(), key=lambda x:x[1], reverse=True)
    
    return [sorted_arr[i][0] for i in range(k)]
    
    """
    freq=counter(arr)
    return [num for num, count in freq.most_common(k)]
    """


    
    
arr=[1,1,2,3,4,2,1,2,1,2]
k=2
print(topk_fre(arr, k))