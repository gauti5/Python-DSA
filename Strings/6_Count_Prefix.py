# Counting words with a given prefix

def count_prefix(words, pref):
    # Optimal Solution
    return sum(1 for word in words if word.startswith(pref))
    
    # Brute Force
    count=0
    n=len(pref)
    for word in words:
        if word[:n]==pref:
            count+=1
    return count    

words=['attention', 'sandeep', 'long', 'attend', 'games', 'attraction']
pref='at'
print(count_prefix(words, pref))