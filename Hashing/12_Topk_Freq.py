# Top K frequent elements

# Leetcode -> 347

# Brute Force 

def topk_fre(arr, k):
    freq=[]
    unq=list(set(arr))
    for n in unq:
        freq.append((n, arr.count(n)))
    freq.sort(key=lambda x:x[1], reverse=True)
    return [freq[i][0] for i in range(k)]

arr=[1,1,2,3,4,2,1,2,1,2]
k=2
print(topk_fre(arr, k))