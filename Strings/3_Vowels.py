# Count the number of vowel strimngs in Range (leetcode - Q2586)

def vowels(words, left, right):
    result=0
    vowels={'a','e','i', 'o', 'u'}
    
    # Oneline same as below steps
    return sum(1 for i in range(left, right+1) if words[i][0] in vowels and words[i][-1] in vowels)


    for i in range(left, right+1):
        word=words[i] # Words
        if word[0] in vowels and word[-1] in vowels: # checking characters in each words like a (first) and e (last)
            result+=1
    return result



words=['a,w,q,e', 'e,w,q', 'a,q,e,r,a', 'i,u,i', 'a,w,q']
left=1
right=4
print(vowels(words, left, right))