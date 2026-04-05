# Permutations in String
from itertools import permutations
def permutations_string(s1, s2):
    
    s1_permutations=set(''.join(p) for p in permutations(s1))
    s1_len=len(s1)
    s2_len=len(s2)
    
    for i in range(s2_len-s1_len+1):
        if s2[i:i+s1_len] in s1_permutations:
            return True
    return False

s1="ab"
s2="ghsgdgabsggygba"

print(permutations_string(s1, s2))