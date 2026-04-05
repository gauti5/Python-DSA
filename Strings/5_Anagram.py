# Valid Anagram (leetcode - Q242)

def anagram(s,t):
    
    # Brute Force
    return sorted(s)==sorted(t)

s='anagram'
t='nagarams'

print(anagram(s,t))