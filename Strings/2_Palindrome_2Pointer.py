# using two pointer

def palindrome(s):
    # two pointer
    new_s=''.join(char.lower() for char in s if char.isalnum())

    left=0
    right=len(new_s)-1
    while left<right:
        if new_s[left]!=new_s[right]:
            return False
        left+=1
        right-=1
    return True

    # Slicing 
    return new_s==new_s[::-1]


s='Sir'
print(palindrome(s))
