# Find the longest palindromic substring..
def isPalindrom(s):
    return s==s[::-1]
def longest(s):
    n=len(s)
    if n==0:
        return ""
    longest=s[0]
    for i in range(n):
        for j in range(i, n):
            sub=s[i:j+1]
            if isPalindrom(sub) and len(sub)>len(longest):
                longest=sub
    return longest
        

s="forgeeksskeegfor"
print(longest(s))