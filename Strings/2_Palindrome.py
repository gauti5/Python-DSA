# Brute Force Approach


s="madam"
new_s=''

# Easy Way
# new_s=''.join(char.lower() for char in s if char.isalnum())

# Brute Force
for char in s:
    for l in char:
        if l.isalnum():
            new_s+=l.lower()
print(new_s)

# Easy Way
# lst=list(new_s)[::-1]
# rev_s=''.join(lst)

# Brute Force
rev_s=''
for c in new_s:
    rev_s=c+rev_s

print(rev_s)