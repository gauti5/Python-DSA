def group_anagram(strs):
    anagram={}
    for word in strs:
        key=''.join(sorted(word))
        if key not in anagram:
            anagram[key]=[]
        anagram[key].append(word)
    return anagram


strs=['eat', 'bat', 'tea', 'ate', 'atb', 'ten']
print(group_anagram(strs))