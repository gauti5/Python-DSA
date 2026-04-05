# First unique character in string (leetcode - Q387)

def unique(string):
    
    # Optimal Solution
    
    cc={}
    for char in string:
        cc[char]=cc.get(char, 0)+1
    
    for i, char in enumerate(string):
        if cc[char]==1:
            return i
    return -1
    
    # O(n^2) Brute Force
    for i in range(len(string)):
        if string.count(string[i])==1:
            return i
    return -1

string='agsfahghsdka'
print(unique(string))