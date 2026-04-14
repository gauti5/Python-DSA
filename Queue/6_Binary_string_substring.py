# Binary String with substrings representing 1 to N

# Leetcode -> 1016

def query_string(s, n):
    substrings=[]
    for i in range(1, n+1):
        sub=bin(i)[2:]
        substrings.append(sub)
    for sub_str in substrings:
        if sub_str not in s:
            return False
    return True

s='0110'
n=4
print(query_string(s, n))