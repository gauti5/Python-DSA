# Reverse the String

def rev(s):
    
    # Two pointer
    n=len(s)
    for i in range(n//2):
        s[i], s[n-1-i]=s[n-1-i], s[i]
    
    # Optimal Approach
    return ''.join(list(a)[::-1])
    lst=list(a)
    final=lst[::-1]
    return ''.join(final) 
    
    # Brute Force Approach
    updated=''
    for i in a:
        updated=i+updated
    return updated

a="Hello"
print(rev(a))