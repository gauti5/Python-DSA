# String Compression (leetcode - Q443)
def string_compress(chars):
    i=0
    n=len(chars)
    s=""

    while i<n:
        count=1
        while i+1<n and chars[i]==chars[i+1]:
            count+=1
            i+=1
        s+=chars[i]
        if count>1:
            s+=str(count)
        i+=1
        
        
    c_len=len(s)
    for j in range(c_len):

        chars[j]=s[j]
    return c_len
    
chars=['a', 'b', 'b', 'b', 'c']
print(string_compress(chars))